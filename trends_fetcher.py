# trends_fetcher.py

import os
import requests
import feedparser
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN  = os.getenv("BALE_BOT_TOKEN")
CHANNEL_ID = os.getenv("BALE_CHANNEL_ID")

def fetch_iran_trends(n=5):
    # آدرس RSS اصلی و هدر مرورگر
    rss_urls = [
        "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IR",
        "https://trends.google.com/trends/trendingsearches/daily/rss?hl=fa&geo=IR&tz=270"
    ]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8"
    }

    for url in rss_urls:
        resp = requests.get(url, headers=headers, timeout=10)
        if resp.status_code == 200:
            feed = feedparser.parse(resp.content)
            if feed.entries:
                return [entry.title for entry in feed.entries[:n]]
    # اگر دو روش هم 404 شد، خالی برگردان
    print(f"خطا در دریافت RSS: همهٔ URLها 404 دادند")
    return []

def post_to_bale(keywords):
    if not keywords:
        return
    message = "🔥 ترندهای داغ امروز ایران:\n\n" + \
              "\n".join(f"{i+1}. {k}" for i, k in enumerate(keywords))
    url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": CHANNEL_ID, "text": message})
    print(resp.status_code, resp.text)

if __name__ == "__main__":
    trends = fetch_iran_trends()
    print("Fetched trends:", trends)
    post_to_bale(trends)
