# test_post.py

import os
import requests
from dotenv import load_dotenv

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# خواندن توکن و شناسه کانال
token = os.getenv("EITAA_API_TOKEN")
chat_id = os.getenv("EITAA_CHANNEL_ID")

# ساخت URL صحیح برای ارسال پیام از طریق پنل EitaaYar
url = f"https://eitaayar.ir/api/{token}/sendMessage"
params = {
    "chat_id": chat_id,
    "text": "✅ ربات ابزار نوین با موفقیت به کانال متصل شد!"
}

# ارسال درخواست (SSL غیرفعال برای تست)
resp = requests.post(url, data=params, verify=False)

# چاپ کد وضعیت و متن پاسخ برای عیب‌یابی
print(resp.status_code, resp.text)
