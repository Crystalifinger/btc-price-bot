import os
import requests
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL"]


def get_btc_price():
    url = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return float(response.json()["price"])


def main():
    price = get_btc_price()

    message = f"""₿ BTC Price

💰 ${price:,.2f}

🔄 Updated every 5 minutes"""

    bot = Bot(token=TOKEN)
    bot.send_message(
        chat_id=CHANNEL,
        text=message
    )


if __name__ == "__main__":
    main()
