
# https://sv443.net/jokeapi/v2/
import pandas as pd
import json
import requests

url = (
    f'https://v2.jokeapi.dev/joke/Any?type=single&amount=5'
)

response = requests.get(url)
data = response.json()

jokes = data['jokes']

# Convert the list of articles into a DataFrame
df_jokes = pd.DataFrame(jokes)

columns = ['id', 'category', 'joke', 'safe']
df = df_jokes[columns]

first_safe_joke = df_jokes[df_jokes['safe'] == 1]['joke'].iloc[0]
print(first_safe_joke)