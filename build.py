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

    # Build index.html from src/index.md
    index_path = SRC / "index.md"
    if index_path.exists():
        meta, body = load_yaml_frontmatter(index_path)
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

    print(f"\n✅ Site généré dans /{DIST}")

if __name__ == "__main__":
    build()
