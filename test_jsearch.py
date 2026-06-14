import requests
from config.settings import RAPIDAPI_KEY

print("API Key Loaded:", RAPIDAPI_KEY is not None)

url = "https://jsearch.p.rapidapi.com/search"

querystring = {
    "query": "Python Developer in India",
    "page": "1",
    "num_pages": "1"
}

headers = {
    "X-RapidAPI-Key": RAPIDAPI_KEY,
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

response = requests.get(
    url,
    headers=headers,
    params=querystring
)

print("Status Code:", response.status_code)
print("Response:")
print(response.text[:2000])