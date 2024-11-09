import requests
from bs4 import BeautifulSoup

url = "https://ident.me/"
proxies = {
    'http': 'http://113.160.218.14:8888',
    'https': 'http://113.160.218.14:8888'  # Added HTTPS proxy
}

file = requests.get(url, proxies=proxies)
print(file.text)
