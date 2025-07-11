# trends_fetcher.py

from pytrends.request import TrendReq
import requests
import os
from dotenv import load_dotenv

# بارگذاری تنظیمات
load_dotenv()
BOT_TOKEN  = os.getenv("BALE_BOT_TOKEN")
CHANNEL_ID = os.getenv("BALE_CHANNEL_ID")

def fetch_iran_trends(n=5):
    pytrends = TrendReq(hl='fa', tz=270)  # بدون پارامترهای اضافی
    try:
        df = pytrends.trending_searches(pn='iran')
        return df[0].tolist()[:n]
    except Exception as e:
        print("خطا در دریافت ترندها:", e)
        return []

def post_to_bale(keywords):
    if not keywords:
        return
    message = "🔥 ترندهای داغ امروز ایران:\n\n"
    for i, kw in enumerate(keywords, 1):
        message += f"{i}. {kw}\n"
    url = f"https://tapi.bale.ai/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHANNEL_ID, "text": message}
    resp = requests.post(url, json=payload)
    print(resp.status_code, resp.text)

if __name__ == "__main__":
    trends = fetch_iran_trends()
    print("Fetched trends:", trends)
    post_to_bale(trends)
