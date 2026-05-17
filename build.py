#!/usr/bin/env python3
"""
Generateur de site statique pour pascalgagnon.ca
Stack : Python + Jinja2 + Markdown + PyYAML
Usage : python3 build.py
"""

import shutil
import yaml
import markdown
from datetime import date
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

SRC = Path("src")
DIST = Path("dist")
LAYOUTS = SRC / "_layouts"
INCLUDES = SRC / "_includes"
DATA = SRC / "_data"
ASSETS = SRC / "assets"

SKIP_COPY_EXTENSIONS = {".docx", ".doc", ".xlsx", ".xls", ".pptx", ".ppt", ".odt", ".pages"}

md = markdown.Markdown(extensions=["meta", "fenced_code", "tables"])


def load_yaml_frontmatter(filepath):
    text = Path(filepath).read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return meta, body
    return {}, text


def load_data(name):
    path = DATA / f"{name}.yaml"
    if path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {}


def collect_all_articles(src):
    """Scanne tous les .md et retourne ceux qui ont un champ system:.
    Cherche d'abord dans src/systemes/cX/ (nouvelle architecture),
    puis dans les anciens verticaux restants (retro-compatibilite).
    """
    all_articles = []
    scan_dirs = []

    # Nouvelle architecture : src/systemes/cX/
    src_systemes = src / "systemes"
    if src_systemes.exists():
        for cx_dir in sorted(src_systemes.iterdir()):
            if cx_dir.is_dir():
                scan_dirs.append((cx_dir, "systemes/" + cx_dir.name))

    # Anciens verticaux (retro-compatibilite si des .md y restent)
    skip = {"_layouts", "_includes", "_data", "assets", "sante-metabolique", "articles",
            "systemes", "reset-method", "blog", "posts"}
    for d in sorted(src.iterdir()):
        if d.is_dir() and d.name not in skip and not d.name.startswith("_"):
            scan_dirs.append((d, d.name))

    for d, src_dir_name in scan_dirs:
        if not d.exists():
            continue
        for md_file in sorted(d.glob("*.md")):
            meta, _ = load_yaml_frontmatter(md_file)
            if not meta.get("system"):
                continue
            meta["src_dir"] = src_dir_name
            meta.setdefault("slug", md_file.stem)
            all_articles.append(meta)
    return all_articles


def build_systems(env, site, all_articles, dist):
    """Genere /systemes/cX/index.html pour les 12 systemes."""
    systemes_data = load_data("systemes")
    systemes = systemes_data.get("systemes", {})
    if not systemes:
        print("! build_systems: systemes.yaml introuvable ou vide")
        return
    template = env.get_template("systeme.html.j2")
    systemes_dist = dist / "systemes"
    systemes_dist.mkdir(exist_ok=True)
    by_system = {}
    for art in all_articles:
        sid = art.get("system")
        if sid:
            by_system.setdefault(sid, []).append(art)
    for sid, sys_meta in systemes.items():
        arts = by_system.get(sid, [])
        out_dir = systemes_dist / sid
        out_dir.mkdir(exist_ok=True)
        html = template.render(site=site, system=sys_meta, articles=arts)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print("+ systemes/" + sid + "/index.html (" + str(len(arts)) + " article(s))")


def build_system_articles(env, site, articles_data, dist):
    """Genere /systemes/cX/[slug]/index.html pour chaque article .md dans src/systemes/cX/.
    Supporte le layout sante-metabolique.html.j2 (injection d image entre sections).
    """
    src_systemes = SRC / "systemes"
    if not src_systemes.exists():
        return
    for cx_dir in sorted(src_systemes.iterdir()):
        if not cx_dir.is_dir():
            continue
        for md_file in sorted(cx_dir.glob("*.md")):
            meta, body = load_yaml_frontmatter(md_file)
            layout_name = meta.get("layout", "article.html.j2")
            try:
                template = env.get_template(layout_name)
            except Exception:
                template = env.get_template("article.html.j2")
            md.reset()
            content_html = md.convert(body)
            content_before = content_html
            content_after = ""
            if layout_name == "sante-metabolique.html.j2" and meta.get("image_info"):
                hr_tag = "<hr />"
                split_position = meta.get("image_info_after_section", 2)
                hr_parts = content_html.split(hr_tag)
                if len(hr_parts) > split_position:
                    content_before = hr_tag.join(hr_parts[:split_position]) + hr_tag
                    content_after = hr_tag.join(hr_parts[split_position:])
            slug = meta.get("slug", md_file.stem)
            out_dir = dist / "systemes" / cx_dir.name / slug
            out_dir.mkdir(parents=True, exist_ok=True)
            meta["page_url"] = f"/systemes/{cx_dir.name}/{slug}/"
            html = template.render(
                site=site, page=meta,
                content=content_html,
                content_before=content_before,
                content_after=content_after,
                articles=articles_data
            )
            (out_dir / "index.html").write_text(html, encoding="utf-8")
            print("+ systemes/" + cx_dir.name + "/" + slug + "/index.html")


def build_vertical(src_dir, dist_dir, env, site, articles, default_layout="article.html.j2"):
    dist_dir.mkdir(exist_ok=True)
    vname = src_dir.name
    for item in sorted(src_dir.iterdir()):
        if item.is_dir():
            dest = dist_dir / item.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
            print("+ " + vname + "/" + item.name + "/ (static)")
        elif item.suffix == ".md":
            meta, body = load_yaml_frontmatter(item)
            layout_name = meta.get("layout", default_layout)
            try:
                template = env.get_template(layout_name)
            except Exception:
                template = env.get_template("base.html.j2")
            md.reset()
            content_html = md.convert(body)
            slug = meta.get("slug", item.stem)
            out_dir = dist_dir / slug
            out_dir.mkdir(exist_ok=True)
            html = template.render(site=site, page=meta, content=content_html, articles=articles)
            (out_dir / "index.html").write_text(html, encoding="utf-8")
            print("+ " + vname + "/" + slug + "/index.html")
        elif item.is_file() and item.suffix.lower() not in SKIP_COPY_EXTENSIONS:
            shutil.copy(item, dist_dir / item.name)
            if item.name == "index.html":
                print("+ " + vname + "/index.html (static)")


def _parse_date(raw, fallback):
    """Convertit une date en ISO 8601 (YYYY-MM-DD), supporte format FR et ISO."""
    if not raw:
        return fallback
    s = str(raw).strip()
    # Deja ISO
    import re
    if re.match(r'\d{4}-\d{2}-\d{2}', s):
        return s[:10]
    # Format francais : "11 mai 2026"
    mois_fr = {
        "janvier": "01", "fevrier": "02", "février": "02",
        "mars": "03", "avril": "04", "mai": "05", "juin": "06",
        "juillet": "07", "aout": "08", "août": "08",
        "septembre": "09", "octobre": "10", "novembre": "11", "decembre": "12", "décembre": "12"
    }
    parts = s.lower().split()
    if len(parts) == 3:
        jour, mois, annee = parts
        m = mois_fr.get(mois)
        if m:
            return f"{annee}-{m}-{int(jour):02d}"
    return fallback


def build_sitemap(all_articles_meta, dist, site):
    """Genere dist/sitemap.xml avec toutes les pages du site."""
    base_url = site.get("url", "https://pascalgagnon.ca").rstrip("/")
    today = date.today().isoformat()
    urls = []

    urls.append({"loc": base_url + "/", "priority": "1.0", "changefreq": "weekly", "lastmod": today})
    urls.append({"loc": base_url + "/systemes/explorer.html", "priority": "0.8", "changefreq": "monthly", "lastmod": today})

    systemes_data = load_data("systemes")
    systemes = systemes_data.get("systemes", {})
    for sid in sorted(systemes.keys()):
        urls.append({"loc": f"{base_url}/systemes/{sid}/", "priority": "0.8", "changefreq": "weekly", "lastmod": today})

    for art in all_articles_meta:
        src_dir = art.get("src_dir", "")
        slug = art.get("slug", "")
        if src_dir.startswith("systemes/") and slug:
            cx = src_dir.split("/")[1]
            art_date = _parse_date(art.get("date"), today)
            urls.append({"loc": f"{base_url}/systemes/{cx}/{slug}/", "priority": "0.7", "changefreq": "monthly", "lastmod": art_date})

    articles_src = SRC / "articles"
    if articles_src.exists():
        for md_file in sorted(articles_src.glob("*.md")):
            meta, _ = load_yaml_frontmatter(md_file)
            slug = meta.get("slug", md_file.stem)
            art_date = _parse_date(meta.get("date"), today)
            urls.append({"loc": f"{base_url}/articles/{slug}/", "priority": "0.7", "changefreq": "monthly", "lastmod": art_date})

    if (SRC / "confidentialite.md").exists():
        urls.append({"loc": f"{base_url}/confidentialite/", "priority": "0.3", "changefreq": "yearly", "lastmod": today})

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u in urls:
        lines += [
            "  <url>",
            f"    <loc>{u['loc']}</loc>",
            f"    <lastmod>{u['lastmod']}</lastmod>",
            f"    <changefreq>{u['changefreq']}</changefreq>",
            f"    <priority>{u['priority']}</priority>",
            "  </url>",
        ]
    lines.append("</urlset>")
    (dist / "sitemap.xml").write_text("\n".join(lines), encoding="utf-8")
    print("+ sitemap.xml (" + str(len(urls)) + " URLs)")


def build():
    if DIST.exists():
        try:
            shutil.rmtree(DIST)
            DIST.mkdir()
        except PermissionError:
            for f in DIST.rglob("*"):
                if f.is_file():
                    try:
                        f.unlink()
                    except Exception:
                        pass
    else:
        DIST.mkdir(parents=True, exist_ok=True)

    if ASSETS.exists():
        shutil.copytree(ASSETS, DIST / "assets")

    env = Environment(
        loader=FileSystemLoader([str(LAYOUTS), str(INCLUDES)]),
        autoescape=False
    )

    site = load_data("site")
    articles = load_data("articles")

    # Page d accueil
    index_html_path = SRC / "index.html"
    index_md_path = SRC / "index.md"
    if index_html_path.exists():
        shutil.copy(index_html_path, DIST / "index.html")
        print("+ index.html (static)")
    elif index_md_path.exists():
        meta, body = load_yaml_frontmatter(index_md_path)
        layout_name = meta.get("layout", "base.html.j2")
        template = env.get_template(layout_name)
        content_html = md.convert(body) if body else ""
        html = template.render(site=site, page=meta, content=content_html, articles=articles)
        (DIST / "index.html").write_text(html, encoding="utf-8")
        print("+ index.html")

    # Pages racine .md
    for md_file in sorted(SRC.glob("*.md")):
        if md_file.name == "index.md":
            continue
        meta, body = load_yaml_frontmatter(md_file)
        layout_name = meta.get("layout", "base.html.j2")
        try:
            template = env.get_template(layout_name)
        except Exception:
            template = env.get_template("base.html.j2")
        md.reset()
        content_html = md.convert(body)
        slug = meta.get("slug", md_file.stem)
        out_dir = DIST / slug
        out_dir.mkdir(exist_ok=True)
        html = template.render(site=site, page=meta, content=content_html, articles=articles)
        (out_dir / "index.html").write_text(html, encoding="utf-8")
        print("+ " + slug + "/index.html")

    # Sante-metabolique (retro-compatibilite + redirections)
    sante_src = SRC / "sante-metabolique"
    if sante_src.exists():
        sante_dist = DIST / "sante-metabolique"
        sante_dist.mkdir(exist_ok=True)
        sm_index = sante_src / "index.html"
        if sm_index.exists():
            shutil.copy(sm_index, sante_dist / "index.html")
            print("+ sante-metabolique/index.html (static)")
        for md_file in sorted(sante_src.glob("*.md")):
            meta, body = load_yaml_frontmatter(md_file)
            layout_name = meta.get("layout", "sante-metabolique.html.j2")
            try:
                template = env.get_template(layout_name)
            except Exception:
                template = env.get_template("article.html.j2")
            md.reset()
            content_html = md.convert(body)
            content_before = content_html
            content_after = ""
            if meta.get("image_info"):
                hr_tag = "<hr />"
                split_position = meta.get("image_info_after_section", 2)
                hr_parts = content_html.split(hr_tag)
                if len(hr_parts) > split_position:
                    content_before = hr_tag.join(hr_parts[:split_position]) + hr_tag
                    content_after = hr_tag.join(hr_parts[split_position:])
            slug = meta.get("slug", md_file.stem)
            out_dir = sante_dist / slug
            out_dir.mkdir(exist_ok=True)
            html = template.render(
                site=site, page=meta,
                content=content_html,
                content_before=content_before,
                content_after=content_after,
                articles=articles
            )
            (out_dir / "index.html").write_text(html, encoding="utf-8")
            print("+ sante-metabolique/" + slug + "/index.html")
        # Copier les redirections meta-refresh (sous-dossiers avec index.html)
        for sub in sorted(sante_src.iterdir()):
            if sub.is_dir():
                redirect_index = sub / "index.html"
                if redirect_index.exists():
                    dest = sante_dist / sub.name
                    dest.mkdir(exist_ok=True)
                    shutil.copy(redirect_index, dest / "index.html")
                    print("+ sante-metabolique/" + sub.name + "/index.html (redirect)")

    # Tous les autres verticaux (generique)
    SKIP_VERTICALS = {
        "_layouts", "_includes", "_data", "assets",
        "sante-metabolique", "systemes",
    }
    for vertical_dir in sorted(SRC.iterdir()):
        if not vertical_dir.is_dir():
            continue
        if vertical_dir.name in SKIP_VERTICALS or vertical_dir.name.startswith("_"):
            continue
        build_vertical(vertical_dir, DIST / vertical_dir.name, env, site, articles)

    # Pages systemes auto-generees (/systemes/c1/, /systemes/c2/, ...)
    all_articles_meta = collect_all_articles(SRC)
    build_systems(env, site, all_articles_meta, DIST)

    # Articles individuels dans /systemes/cX/[slug]/
    build_system_articles(env, site, articles, DIST)

    # Copier les fichiers statiques de src/systemes/ (explorer.html, etc.)
    src_systemes = SRC / "systemes"
    if src_systemes.exists():
        dist_systemes = DIST / "systemes"
        dist_systemes.mkdir(exist_ok=True)
        for f in src_systemes.iterdir():
            if f.is_file() and f.suffix.lower() not in SKIP_COPY_EXTENSIONS:
                shutil.copy(f, dist_systemes / f.name)
                print("+ systemes/" + f.name + " (static)")

    # Fichiers statiques racine (404.html, robots.txt)
    for fname in ["404.html", "robots.txt"]:
        src_file = SRC / fname
        if src_file.exists():
            shutil.copy(src_file, DIST / fname)
            print("+ " + fname + " (static)")

    # Sitemap
    build_sitemap(all_articles_meta, DIST, site)

    print("\nSite genere dans /" + str(DIST))


if __name__ == "__main__":
    build()
