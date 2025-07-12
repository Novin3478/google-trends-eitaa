# trends_fetcher.py

import requests
import xml.etree.ElementTree as ET
import os
from dotenv import load_dotenv

# بارگذاری تنظیمات از .env
load_dotenv()
BOT_TOKEN  = os.getenv("BALE_BOT_TOKEN")
CHANNEL_ID = os.getenv("BALE_CHANNEL_ID")

def fetch_iran_trends(n=5):
    # RSS رسمی Google Trends برای ایران
    rss_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=IR"
    resp = requests.get(rss_url)
    root = ET.fromstring(resp.content)
    items = root.findall(".//item")
    trends = [item.find("title").text for item in items[:n]]
    return trends

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
