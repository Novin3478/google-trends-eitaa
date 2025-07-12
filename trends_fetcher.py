# trends_fetcher.py

import os
import re
import requests
from dotenv import load_dotenv

load_dotenv()
BOT_TOKEN  = os.getenv("BALE_BOT_TOKEN")
CHANNEL_ID = os.getenv("BALE_CHANNEL_ID")

def fetch_iran_trends(n=5):
    url = "https://trends.google.com/trends/trendingsearches/daily?geo=IR"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
        "Accept-Language": "fa-IR,fa;q=0.9,en;q=0.8"
    }
    resp = requests.get(url, headers=headers, timeout=10)
    if resp.status_code != 200:
        print(f"خطا در دریافت HTML: HTTP {resp.status_code}")
        return []
    # با regex عناوین را بگیرید
    titles = re.findall(r'"title":"([^"]+)"', resp.text)
    # عناوین اول هر جعبه trend را برداریم
    seen, trends = set(), []
    for t in titles:
        if t not in seen:
            seen.add(t)
            trends.append(t)
        if len(trends) >= n:
            break
    return trends

def post_to_bale(keywords):
    if not keywords:
        print("هیچ ترندی پیدا نشد.")
        return
    message = "🔥 ترندهای داغ امروز ایران:\n\n" + "\n".join(f"{i+1}. {k}" for i, k in enumerate(keywords))
    url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"
    resp = requests.post(url, json={"chat_id": CHANNEL_ID, "text": message})
    print(resp.status_code, resp.text)

if __name__ == "__main__":
    trends = fetch_iran_trends()
    print("Fetched trends:", trends)
    post_to_bale(trends)
