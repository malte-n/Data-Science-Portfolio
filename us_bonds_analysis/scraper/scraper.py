from bs4 import BeautifulSoup
from urllib.request import urlopen


def get_etf_prices():
    etfs = [
        "https://www.ishares.com/us/products/239566/ishares-iboxx-investment-grade-corporate-bond-etf",
        "https://www.ishares.com/us/products/239468/ishares-us-treasury-bond-etf",
        "https://www.ishares.com/us/products/239655/ishares-msci-global-metals-mining-producers-etf",
        "https://www.ishares.com/us/products/239561/ishares-gold-trust-fund",
    ]

    etf_prices = {}

    for etf in etfs:
        html = urlopen(
            etf
        )
        soup = BeautifulSoup(html.read(), "html.parser")
        name = soup.find('h1', {'class': 'product-title'})
        price = soup.find('span', {'class': 'header-nav-data'})
        #price = price.text.strip('$')
        name = name.text
        price = price.text
        name = name.replace('\r', '')
        name = name.replace('\n', '')
        price = price.replace('\n', '')
        price = price.replace('$', '')
        #price = price.replace('.', ',')

        etf_prices[name] = float(price)

    return etf_prices

print(get_etf_prices())
