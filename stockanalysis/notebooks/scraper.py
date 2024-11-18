# https://webscraper.io/test-sites/tables

from bs4 import BeautifulSoup
import requests

url = "https://webscraper.io/test-sites/tables" 

response = requests.get(url)
print(response)