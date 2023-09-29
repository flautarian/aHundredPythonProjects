import datetime as dt
import json
import os
import requests

# Const info
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# API KEYS
ALPHAVANTAGE_API_KEY = os.environ["ALPHAVANTAGE_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_API_KEY = os.environ["NEWS_API_KEY"]
TWILIO_SID = os.environ["TWILIO_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWILIO_AUTH_TOKEN"]

#Endpoints
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

df = dt.datetime.now() - dt.timedelta(days=2)
dt = dt.datetime.now() - dt.timedelta(days=1)

alphavantage_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
}

r = requests.get(STOCK_ENDPOINT, params=alphavantage_params)

data = r.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]

#Get the day before yesterday's closing stock price
day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]

print(f"{yesterday_closing_price} - {day_before_yesterday_closing_price}")

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

diff = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


#Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diff_percent = round((diff / float(yesterday_closing_price)) * 100)
print(diff_percent)


## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

if abs(diff_percent) > 1:
    news_params = {
        "apiKey": NEWS_API_KEY,
        "qInTitle": COMPANY_NAME,
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    #Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation
    three_articles = articles[:3]
    print(three_articles)

    ## STEP 3: Use Twilio to send a seperate message with each article's title and description to your phone number.

    #Create a new list of the first 3 article's headline and description using list comprehension.
    formatted_articles = [f"{STOCK}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
    print(formatted_articles)
    #Send each article as a separate message via Twilio.
    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    #TODO 8. - Send each article as a separate message via Twilio.
    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )

