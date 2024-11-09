import pandas as pd
from bs4 import BeautifulSoup
import requests
import pendulum

ltps = []
share = []
profit = []
def meroshare(compName):
    url = "https://merolagani.com/LatestMarket.aspx"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    result = soup.find('table', {'class':'table table-hover live-trading sortable'})
    rows = result.find_all('tr')
    for row in rows:
        columns = row.find_all('td')
        if columns:
            symbol = columns[0].text.strip()
            if symbol==compName:
                ltp = columns[1].text.replace(',', '')
                return float(ltp)

def compShare():
    while True:
        company = input("Enter Company Name: ")
        currentValue = meroshare(company.upper())
        if currentValue is None:
            print("Try Again")
            continue
        print(f'{company}:{currentValue}')
        kitta = int(input("No of Kitta: "))
        oldValue = float(input("Price you bought share with: "))
        total = float(kitta*(currentValue - oldValue))
        time = pendulum.now()

        if total>0:
            print(f'As of {time} your profit is {total}')
        elif total==0:
            print(f'As of {time} you are in neutral.')
        else:
            print(f'As of {time} you are at loss of {total}')
        final = input("Do you want to search more (Y/N)")
        if final.upper() !='Y':
            break
        share.append(company)
        profit.append(total)
        ltps.append(currentValue)

def main():
    info = compShare()
    df = pd.DataFrame({'Share':share, 'Current Value':ltps, 'Profit':profit})
    toCSV = df.to_csv('result.csv', index=False)
    print(f'Saved to {toCSV}')
if __name__ == "__main__":
    main()