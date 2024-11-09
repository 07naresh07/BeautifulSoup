from bs4 import BeautifulSoup

text = "<html><p><head>The king and his Soldiers</head><p><stong></p><body>'I want to go home, king said and he rode his horse.'</body><p><html>"
soup = BeautifulSoup(text, 'html.parser')
#print(soup.prettify())
print(soup.head)
print(soup.body)
