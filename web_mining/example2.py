from bs4 import BeautifulSoup
import requests

url = 'http://www.google.com/search?q=css'
response = requests.get(url)
if not response.status_code == 200:
    print('An error has occurred.')
    exit()
else:
    print('Success!')
    soup = BeautifulSoup(response.text, 'html5lib')
    print(soup.prettify())

    # get all heading h1
    headings_1 = soup.find_all('h1')
    print("Headings 1:")
    for i in headings_1:
        print(i.text)
    headings_3 = soup.find_all('h3')
    print("Headings 3:")
    for i in headings_3:
        print(i.text)
    
    # get all the links
    links = soup.find_all('a')
    print("Links:")
    for i in links:
        print(f'{i.text} & {i.get("href")}')