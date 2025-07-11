import requests

# توکن و آیدی کانال
TOKEN = "432025980:qc2Ueqf28oCmYHUT2B1KWABHtVgf1J9lnJS5ehhf"
CHANNEL_ID = "@Novin_Abzaar"
MESSAGE = "✅ تست موفقیت‌آمیز ارسال پیام از طریق ربات نوین ابزار!"

# آدرس API برای ارسال پیام
url = f"https://tapi.bale.ai/bot{TOKEN}/sendMessage"

# پارامترها
data = {
    "chat_id": CHANNEL_ID,
    "text": MESSAGE
}

# ارسال درخواست
response = requests.post(url, json=data)

# نمایش نتیجه
print(response.status_code)
print(response.text)
