import requests

url = "https://api.telegram.org/bot5268748619%3AAAGHo1QI6eNRp_Vw3dor28XtwIqJocmJm10/sendPhoto"



payload = {
    "photo": "https://pbs.twimg.com/media/FSATBDHXMAA6yhc?format=jpg&name=4096x4096",
    "caption": "BNBUSDT | BINANCE",
    "disable_notification": False,
    "reply_to_message_id": None,
    "chat_id": "@volumeallert"
}
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)