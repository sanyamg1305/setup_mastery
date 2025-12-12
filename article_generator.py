import csv
from pathlib import Path
import sys
ART_DIR = Path("src/content/articles")
ART_DIR.mkdir(parents=True, exist_ok=True)

def create_article(slug, title, content, meta_tags=""):
    filename = ART_DIR / f"{slug}.md"
    front = f"""---
title: "{title}"
date: 2025-12-12
tags: [{meta_tags}]
---
"""
    filename.write_text(front + "\n" + content)
    print("Created", filename)

def main(csv_path):
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            slug = row['slug']
            title = row['title']
            body = row.get('content', '')
            create_article(slug, title, body, row.get('tags',''))

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python article_generator.py articles.csv")
    else:
        main(sys.argv[1])
