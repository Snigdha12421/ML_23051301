# scrape_news.py

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

HN_URL = "https://news.ycombinator.com/"

def fetch_hackernews():
    resp = requests.get(HN_URL, timeout=15)
    resp.raise_for_status()
    return resp.text

def parse_hackernews(html):
    soup = BeautifulSoup(html, "html.parser")

    rows = soup.find_all("tr", class_="athing")

    data = []
    for row in rows:
        # Title & link are under <span class="titleline"><a>
        titleline = row.find("span", class_="titleline")
        a_tag = titleline.find("a") if titleline else None

        title = a_tag.get_text(strip=True) if a_tag else ""
        link = a_tag["href"] if a_tag and a_tag.has_attr("href") else ""

        # Subtext is the next row
        sub = row.find_next_sibling("tr")
        subtext = sub.find("td", class_="subtext") if sub else None

        points = 0
        author = None
        time_ago = None
        comments = None

        if subtext:
            score_span = subtext.find("span", class_="score")
            if score_span:
                points = int(score_span.get_text(strip=True).split()[0])

            user_a = subtext.find("a", class_="hnuser")
            if user_a:
                author = user_a.get_text(strip=True)

            age_span = subtext.find("span", class_="age")
            if age_span:
                time_ago = age_span.get_text(strip=True)

            # Comments = last <a> tag inside subtext
            comment_links = subtext.find_all("a")
            if comment_links:
                comments = comment_links[-1].get("href", "")

        data.append({
            "scraped_at": datetime.utcnow().isoformat() + "Z",
            "title": title,
            "link": link,
            "author": author,
            "points": points,
            "time_ago": time_ago,
            "comments_link": comments
        })

    return data

def save_to_csv(items, filename="hackernews_latest.csv"):
    df = pd.DataFrame(items)
    df.to_csv(filename, index=False)
    return df

def main():
    print("Fetching Hacker News front page...")
    html = fetch_hackernews()
    print("Parsing page...")
    items = parse_hackernews(html)
    print(f"Found {len(items)} items. Saving to CSV...")
    df = save_to_csv(items)
    print("Done. Sample:")
    print(df.head(10).to_string(index=False))

if __name__ == "__main__":
    main()
