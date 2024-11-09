from bs4 import *
import requests
import pandas as pd

bookList = []
currentPage = 1
while True:
    url = "https://books.toscrape.com/catalogue/category/books_1/page-"+str(currentPage)+".html"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'html.parser')
    if soup.title.text=='404 Not Found':
        break
    result = soup.find_all('li', {'class':"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
    for books in result:
        relativeLink = books.find('a').attrs['href']
        fullLink = "https://books.toscrape.com/catalogue/"+relativeLink[6:]
        rating = books.find('p', class_="star-rating")
        if rating:
            rate = rating['class'][1]
        else:
            rate = "No Rating"
        items = {
            "Title" : books.find('img').attrs['alt'],
            "Price" : books.find('p', {'class':"price_color"}).text,
            "Stock" : books.find('p', {'class':"instock availability"}).text.strip(),
            "Link" : fullLink,
            "Rating" : rate
        }
        bookList.append(items)
    currentPage+=1

for books in bookList:  #Calling keys of the dictionary using Value i.e. 'Title' is value and it returns 'Title of the books' based on scrapping method
    print(f"{books['Title']}, {books['Price']}, {books['Stock']}, {books['Link']}, {books['Rating']}")

df = pd.DataFrame(bookList)
df.to_csv('WebScrappingBooks.csv', index=False)