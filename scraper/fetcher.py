import requests
from config import HEADERS

def fetch_page(url):
    response = requests.get(url, headers=HEADERS)
    return response.text