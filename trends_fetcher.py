# trends_fetcher.py

import os
import requests
import feedparser
from dotenv import load_dotenv

# بارگذاری تنظیمات از .env
load_dotenv()
BOT_TOKEN  = os.getenv("BALE_BOT_TOKEN")
CHANNEL_ID = os.getenv("BALE_CHANNEL_ID")

def fetch_iran_trends(n=5):
    rss_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IR"
    headers = {"User-Agent": "Mozilla/5.0"}  # تقلید مرورگر
    resp = requests.get(rss_url, headers=headers, timeout=10)
    if resp.status_code != 200:
        print(f"خطا در دریافت RSS: HTTP {resp.status_code}")
        return []
    # با feedparser پارس می‌کنیم
    feed = feedparser.parse(resp.content)
    if not feed.entries:
        print("خطا: RSS entry پیدا نشد.")
        return []
    return [entry.title for entry in feed.entries[:n]]

def post_to_bale(keywords):
    if not keywords:
        return
    message = "🔥 ترندهای داغ امروز ایران:\n\n" + "\n".join(f"{i+1}. {k}" for i, k in enumerate(keywords))
    url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": CHANNEL_ID, "text": message})
    print(resp.status_code, resp.text)

if __name__ == "__main__":
    trends = fetch_iran_trends()
    print("Fetched trends:", trends)
    post_to_bale(trends)
