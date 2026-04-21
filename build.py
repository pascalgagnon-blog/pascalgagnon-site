#\!/usr/bin/env python3
"""
Generateur de site statique pour pascalgagnon.ca
Stack : Python + Jinja2 + Markdown + PyYAML
Usage : python3 build.py
"""

import shutil
import yaml
import markdown
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


def build_vertical(src_dir, dist_dir, env, site, articles, default_layout="article.html.j2"):
    dist_dir.mkdir(exist_ok=True)
    vname = src_dir.name

    for item in sorted(src_dir.iterdir()):
        if item.is_dir():
            dest = dist_dir / item.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
            print(f"+ {vname}/{item.name}/ (static)")

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
            html = template.render(
                site=site, page=meta, content=content_html, articles=articles
            )
            (out_dir / "index.html").write_text(html, encoding="utf-8")
            print(f"+ {vname}/{slug}/index.html")

        elif item.is_file() and item.suffix.lower() not in SKIP_COPY_EXTENSIONS:
            shutil.copy(item, dist_dir / item.name)
            if item.name == "index.html":
                print(f"+ {vname}/index.html (static)")


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

    # Page d'accueil
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

    # Pages racine .md (ex: a-propos.md)
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
        print(f"+ {slug}/index.html")

    # Sante-metabolique (special: injection image entre sections)
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
            print(f"+ sante-metabolique/{slug}/index.html")

    # Tous les autres verticaux (generique)
    SKIP_VERTICALS = {"_layouts", "_includes", "_data", "assets", "sante-metabolique"}
    for vertical_dir in sorted(SRC.iterdir()):
        if not vertical_dir.is_dir():
            continue
        if vertical_dir.name in SKIP_VERTICALS or vertical_dir.name.startswith("_"):
            continue
        build_vertical(vertical_dir, DIST / vertical_dir.name, env, site, articles)

    print(f"\nSite genere dans /{DIST}")


if __name__ == "__main__":
    build()
