
# -----------------------------------Imports
import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv


# --------------------------------Get secrets
load_dotenv("C:/Users/Popuś/Desktop/Python/environment_variables/.env")
# dotenv_path = join(dirname(__file__), '.env')
# load_dotenv(dotenv_path)

STOCK_API_KEY = os.getenv("api_key_stockapi")
NEWS_API_KEY = os.getenv("api_key_newsapi")

# ------------------------------------Company info
STOCK_NAME = "SHEL"  # only 4 letters
COMPANY_NAME = "Shell plc"

# ------------------------------------Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

# ---------------------------------Get yesterday's closing stock price.
stock_params = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
# data = response.json()
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
# yesterday_closing_price = yesterday_data["4. close"]
yesterday_closing_price = 202.2
# ----------------------------Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]


# ---------------------------------Find the positive difference between prices
# difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
difference = 55.7
# ----------------------------Use emojii to show difference
arrow = None
if difference > 0:
    arrow = "🔺"
else:
    arrow = "🔻"

# ---------------------The percentage difference in price between closing prices
diff_percent = round((abs(difference) / float(yesterday_closing_price)) * 100)

# Use the News API to get articles
news_params = {
    "apiKey": NEWS_API_KEY,
    "q": COMPANY_NAME,
    "pageSize": 10,
}
news_response = requests.get(NEWS_ENDPOINT, params=news_params)
three_articles = news_response.json()["articles"][0:3]


# ------------------------Create a new list of the first 3 article's headline and description using list comprehension.
formatted_articles = [
    f'{STOCK_NAME}: {arrow} {diff_percent}% \nHeadline: {article["title"]}. \nBrief: {article["description"]} {article["url"]}' for article in three_articles]
# print(formatted_articles) - list with 3 strings


title_articles = [f'{article["title"]}' for article in three_articles]
description_articles = [f'{article["description"]}' for article in three_articles]
url_articles = [f'{article["url"]}' for article in three_articles]


class Article():
    def __init__(self, title, description, url):
        self.title = title
        self.description = description
        self.url = url

