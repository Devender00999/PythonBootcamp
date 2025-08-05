import requests 
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import os
from dotenv import load_dotenv

load_dotenv()


NEWS_API_KEY = os.getenv('NEWS_API_KEY')
STOCK_API_KEY = os.getenv('STOCK_API_KEY')
## STEP 1: Use https://www.alphavantage.co

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
params = {
   "function": "TIME_SERIES_DAILY",
   "symbol": "IBM",
   # "outputsize": "full",
   "apikey": STOCK_API_KEY
}

res = requests.get('https://www.alphavantage.co/query', params=params)
res.raise_for_status()
result = res.json()
print(result)
yesterday_close = float(result['Time Series (Daily)']["2025-08-01"]['4. close'])
day_before_yes_close = float(result['Time Series (Daily)']['2025-07-31']['4. close'])
diff = round(((day_before_yes_close - yesterday_close) / day_before_yes_close) * 100,2)

print(diff)
if abs(diff) > 5:
   print("Get news")
   
def get_news(company: str):
   new_params = {
      "q": company,
      "from": "2025-07-05",
      "sortBy": "publishedAt",
      "apiKey": NEWS_API_KEY,
      "page": 1
   }
   res = requests.get("https://newsapi.org/v2/everything", params=new_params)
   res.raise_for_status()
   return res.json()

print(get_news("tesla"))

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

