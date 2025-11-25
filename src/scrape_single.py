#!/usr/bin/env python3
import json
from newspaper import Article
from pathlib import Path
import sys

OUT_DIR = Path("../data/raw")
OUT_DIR.mkdir(parents=True, exist_ok=True)

def fetch_and_save(url, out_filename="sample_article.json"):
    a = Article(url)
    a.download()
    a.parse()
    article = {
        "url": url,
        "title": a.title or "",
        "authors": a.authors or [],
        "publish_date": str(a.publish_date) if a.publish_date else None,
        "text": a.text or "",
    }
    out_path = OUT_DIR / out_filename
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(article, f, ensure_ascii=False, indent=2)
    print(f"Saved article to {out_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python src/scrape_single.py <article_url>")
        sys.exit(1)
    url = sys.argv[1]
    fetch_and_save(url)
