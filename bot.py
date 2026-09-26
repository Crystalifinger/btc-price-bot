import os
import requests
from telegram import Bot

TOKEN = os.environ["BOT_TOKEN"]
CHANNEL = os.environ["CHANNEL"]


def get_btc_price():
    url = "https://pro-api.coinmarketcap.com/public-api/v2/simple/price"

    params = {
        "symbol": "BTC",
        "convert": "USD"
    }

    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()

    data = response.json()

    price = data["data"]["BTC"]["quote"]["USD"]["price"]

    return float(price)


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
