import requests
import pandas as pd

BASE_URL = "https://ghoapi.azureedge.net/api"


def get_dataset(dataset_name):
    """
    Download WHO dataset.
    """

    url = f"{BASE_URL}/{dataset_name}"

    response = requests.get(url)

    response.raise_for_status()

    data = response.json()

    return pd.DataFrame(data["value"])


def save_raw_data(df, filename):

    path = f"H:/DE/who-tb-analysis/data/raw/{filename}"

    df.to_csv(
        path,
        index=False
    )

    print(f"Saved: {path}")

    
    