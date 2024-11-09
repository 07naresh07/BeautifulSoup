import pandas as pd
from bs4 import *
import requests

words = []
meanings  = []
while True:
    word = input('Enter word or QUIT to exit    ')
    if word.lower()=='quit':
        break
    else:
        url = f"https://www.merriam-webster.com/dictionary/{word}"
        data = requests.get(url)
        if data.status_code!=200:
            print('ERROR')
            continue
        soup = BeautifulSoup(data.text, 'html.parser')
        result = soup.find('span', class_='dtText')
        if result:
            meaning = result.text.strip()
            print(f'Word: {word}, \nMeaning: {meaning}')
            words.append(word)
            meanings.append(meaning)
        else:
            print(f'Please check the meaning of {word} and try again')

df = pd.DataFrame({'Words':words, 'Meanings':meanings})
df.to_csv('WebScrapping.csv', index=False)