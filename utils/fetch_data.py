import requests
import pandas as pd
from config import ACLED_API_KEY, ACLED_EMAIL, ACLED_API_URL

def get_acled_data(country="Nigeria", limit=1000):
    url = f"{ACLED_API_URL}/"
    params = {
        "key": ACLED_API_KEY,
        "email": ACLED_EMAIL,
        "format": "json",
        "country": country,
        "limit": limit,
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            df = pd.DataFrame(data["data"])
            return df
        else:
            return pd.DataFrame()
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
