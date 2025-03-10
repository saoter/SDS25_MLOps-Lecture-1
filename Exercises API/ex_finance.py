# https://www.alphavantage.co/

import os
from dotenv import load_dotenv
import pandas as pd
import json
import requests

load_dotenv()

# IMPORTANT... you have to get your API KEY from Alhavantage, and save it in '.env' file, as FIN_API_KEY=XXXXXXXXXXXXXX


api_key = os.getenv('FIN_API_KEY')


url = (
    f'https://www.alphavantage.co/query?'
    f'function=TIME_SERIES_DAILY&'
    f'symbol=AAPL&'
    f'apikey={api_key}'
)

#print(url)

response = requests.get(url)

data = response.json()


# Convert the list of articles into a DataFrame
finance = data['Time Series (Daily)']
symbol = data['Meta Data']['2. Symbol']


df = pd.DataFrame(finance)

# Transpose the DataFrame
df_transposed = df.transpose()
df_transposed['Symbol'] = symbol

# Now, each column is an attribute (open, high, low, close, volume) and each row is a date.
print(df_transposed.head())
