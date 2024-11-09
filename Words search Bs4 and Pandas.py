import requests
from bs4 import BeautifulSoup
import pandas as pd

words = []
meanings = []
while True:
    input_word = input("Enter word you want to lookout for or 'quit' to get out!! ")
    if input_word.lower() == 'quit':
        break
    url = "https://www.merriam-webster.com/dictionary/"+input_word
    page = requests.get(url)
    if page.status_code != 200:
        print("No word found")
        continue
    soup = BeautifulSoup(page.text, 'html.parser')
    result = soup.find("span", class_="dtText")
    if result:
        meaning = result.text.strip()
        print("Definition: "+meaning)

        words.append(input_word)
        meanings.append(meaning)
df = pd.DataFrame({'Word':words, "Meaning":meanings})
df.to_csv('Word_Meanings.csv', index=False)
print("List of the words are exported in 'Word_Meanings.csv' file.")



