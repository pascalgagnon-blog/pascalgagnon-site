#!/usr/bin/env python3
"""
Générateur de site statique pour pascalgagnon.ca
Stack : Python + Jinja2 + Markdown + PyYAML
Usage : python3 build.py
"""

import os
import re
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

md = markdown.Markdown(extensions=["meta", "fenced_code", "tables"])

def load_yaml_frontmatter(filepath):
    """Parse YAML frontmatter + body from a .md file."""
    text = Path(filepath).read_text(encoding="utf-8")
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            body = parts[2].strip()
            return meta, body
    return {}, text

def load_data(name):
    """Load a YAML data file from src/_data/."""
    path = DATA / f"{name}.yaml"
    if path.exists():
        return yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return {}

def build():
    # Clean dist (fichiers seulement, garder le dossier si permissions restreintes)
    if DIST.exists():
        try:
            shutil.rmtree(DIST)
            DIST.mkdir()
        except PermissionError:
            for f in DIST.rglob("*"):
                if f.is_file():
                    try: f.unlink()
                    except: pass
    else:
        DIST.mkdir(parents=True, exist_ok=True)

    # Copy assets
    if ASSETS.exists():
        shutil.copytree(ASSETS, DIST / "assets")

    # Jinja2 env
    env = Environment(
        loader=FileSystemLoader([str(LAYOUTS), str(INCLUDES)]),
        autoescape=False
    )

    # Global data
    site = load_data("site")
    articles = load_data("articles")

    # Build index.html — static HTML priority over template
    index_html_path = SRC / "index.html"
    index_md_path = SRC / "index.md"
    if index_html_path.exists():
        shutil.copy(index_html_path, DIST / "index.html")
        print("✓ index.html (static)")
    elif index_md_path.exists():
        meta, body = load_yaml_frontmatter(index_md_path)
        layout_name = meta.get("layout", "base.html.j2")
        template = env.get_template(layout_name)
        content_html = md.convert(body) if body else ""
        html = template.render(
            site=site,
            page=meta,
            content=content_html,
            articles=articles,
        )
        (DIST / "index.html").write_text(html, encoding="utf-8")
        print("✓ index.html")

    # Build individual article pages
    articles_src = SRC / "articles"
    if articles_src.exists():
        (DIST / "articles").mkdir(exist_ok=True)
        for md_file in sorted(articles_src.glob("*.md")):
            meta, body = load_yaml_frontmatter(md_file)
            layout_name = meta.get("layout", "article.html.j2")
            try:
                template = env.get_template(layout_name)
            except Exception:
                template = env.get_template("base.html.j2")
            md.reset()
            content_html = md.convert(body)
            slug = meta.get("slug", md_file.stem)
            out_dir = DIST / "articles" / slug
            out_dir.mkdir(exist_ok=True)
            html = template.render(
                site=site,
                page=meta,
                content=content_html,
                articles=articles,
            )
            (out_dir / "index.html").write_text(html, encoding="utf-8")
            print(f"✓ articles/{slug}/index.html")

    # Build sante-metabolique article pages
    sante_metabolique_src = SRC / "sante-metabolique"
    sante_metabolique_mds = sorted(sante_metabolique_src.glob("*.md")) if sante_metabolique_src.exists() else []
    if sante_metabolique_mds:
        (DIST / "sante-metabolique").mkdir(exist_ok=True)
        for md_file in sante_metabolique_mds:
            meta, body = load_yaml_frontmatter(md_file)
            layout_name = meta.get("layout", "sante-metabolique.html.j2")
            try:
                template = env.get_template(layout_name)
            except Exception:
                template = env.get_template("article.html.j2")
            md.reset()
            content_html = md.convert(body)

            # Injecter l'image_info entre la section 1 et la section 2
            # On sépare le contenu après le 2e <hr /> pour positionner l'image
            # au centre de l'article plutôt qu'en bas de page.
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
            out_dir = DIST / "sante-metabolique" / slug
            out_dir.mkdir(exist_ok=True)
            html = template.render(
                site=site, page=meta,
                content=content_html,          # conservé pour rétrocompatibilité
                content_before=content_before,
                content_after=content_after,
                articles=articles
            )
            (out_dir / "index.html").write_text(html, encoding="utf-8")
            print(f"✓ sante-metabolique/{slug}/index.html")

    # Copy sante-metabolique/index.html (listing page) — static or already present
    sm_index_src = sante_metabolique_src / "index.html"
    if sm_index_src.exists():
        (DIST / "sante-metabolique").mkdir(exist_ok=True)
        shutil.copy(sm_index_src, DIST / "sante-metabolique" / "index.html")
        print("✓ sante-metabolique/index.html (static)")

    # Copy static directories (any src/ subdir not prefixed with _ and not articles/assets)
    skip = {"_layouts", "_includes", "_data", "assets", "articles", "sante-metabolique"}
    for item in SRC.iterdir():
        if item.is_dir() and item.name not in skip and not item.name.startswith("_"):
            dest = DIST / item.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(item, dest)
            print(f"✓ static/{item.name}/")

    print(f"\n✅ Site généré dans /{DIST}")

if __name__ == "__main__":
    build()
