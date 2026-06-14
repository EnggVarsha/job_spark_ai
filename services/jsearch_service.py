import requests
from config.settings import RAPIDAPI_KEY

def search_jobs(query):

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "page": "1",
        "num_pages": "1"
    }

    response = requests.get(
        url,
        headers=headers,
        params=params,
        timeout=20
    )

    data = response.json()

    print("Returned Jobs:", len(data.get("data", [])))

    return data.get("data", [])