import requests
from bs4 import *
word = input("Enter a word: ").strip()
url = f"https://www.merriam-webster.com/dictionary/{word}"
data = requests.get(url)
soup = BeautifulSoup(data.text, 'html.parser')
result = soup.find("span", class_="dtText")
if data.status_code!=200:
    print("Word Not Found")
else:
    print(result.text)


