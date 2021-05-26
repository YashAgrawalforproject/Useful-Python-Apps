from bs4 import BeautifulSoup
import requests

#url,req,soup

def parseprice():

    url = 'https://in.finance.yahoo.com/quote/%5EBSESN?P=^BSESN'
    req=requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    price = soup.find('div', {'class': 'D(ib) Mend(20px)'}).find_all('span')
    return price[0].text

while True:
    print('the current price: '+str(parseprice()))







