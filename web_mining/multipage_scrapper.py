from bs4 import BeautifulSoup
import requests
import pandas as pd

# get the data from website as a soup object
def get_soup(url) -> BeautifulSoup:
    try:
        page = requests.get(url)
        if page.status_code == 200:
            return BeautifulSoup(page.content, 'html5lib')
        else:
            print('Error:', page.status_code)
    except Exception as e:
        print('Error:',e)

def collect_items(soup) -> list:
    try:
        items = soup.find_all('div', class_='_1xHGtK _373qXS')
        if len(items) > 0:
            return items
    except Exception as e:
        print('Error:', e)

#extract the data in the form of dictionary
def extract_data(item) -> dict:
    try : brand = item.find('div', class_='_2WkVRV').text
    except : brand = None
    
    try : product = item.find('a', class_='IRpwTa _2-ICcC').text
    except : product = None
    
    try : link = item.find('a', class_='IRpwTa _2-ICcC').attrs.get('href')
    except: link = None
        
    try : price = item.find('div', class_='_30jeq3').text
    except : price = None
    
    try : discount = item.find('div', class_='_3Ay6Sb').text
    except : discount = None
    
    return {
        'brand':brand,
        'description':product,
        'link':link,
        'price':price,
        'discount':discount
    }

# save the data to a csv file
def save_data(data, filename):
    d = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')

# main function to run the program
def main(): 
    s = 'bags'
    page_data = []
    url = f"https://www.flipkart.com/search?q={s}"
    print("URL =>",url)
    soup = get_soup(url)
    items = collect_items(soup)
    if isinstance(items, list):
        print(f'Total items found: {len(items)}')
        for item in items:
            data = extract_data(item)
            page_data.append(data)
            print(data)
        

# call the main function
main()

