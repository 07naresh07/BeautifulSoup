import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/today/l/33ec95eb879a86ed994df81d7b0a74c8b0c3f83868e367b46069b7edd2c04487"
data = requests.get(url)
soup = BeautifulSoup(data.content, 'html.parser')
result = soup.title.text
print(result)
file =soup.find('span', {'data-testid':"TemperatureValue"})
print(file.text)
print(soup.find('div', {'data-testid':"wxPhrase"}).text)

print(soup.find('div', class_='Card--content--1GQMr').text)