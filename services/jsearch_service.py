import os
import requests
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")


def search_jobs(
    query,
    location="India",
    page=1
):

    url = "https://jsearch.p.rapidapi.com/search"

    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": f"{query} in {location}",
        "page": str(page),
        "num_pages": "1"
    }

    try:

        response = requests.get(
            url,
            headers=headers,
            params=params,
            timeout=60
        )

        response.raise_for_status()

        return response.json().get(
            "data",
            []
        )

    except Exception as e:

        st.error(
            f"Error: {str(e)}"
        )

        return []