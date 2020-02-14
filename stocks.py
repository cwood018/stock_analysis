import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime as dt

CRYPO = {
    'name': [],
    'price': [],
    'change': [],
    'percent_change': [],
    'market_cap': [],
    'volume_in_currency': [],
    'circulating_supplies': []
}
CURRENCY = {
    'names': [],
    'last_price': [],
    'change': [],
    'percent_change': []
}
MOST_ACTIVE = {
    'name': [],
    'price': [],
    'change': [],
    'percent_change': [],
    'volume': [],
    'avg_volume': [],
    'market_cap': []
}
COMMODITIES = {
    'name': [],
    'last_price': [],
    'market_time': [],
    'change': [],
    'percent_change': [],
    'volume': [],
    'open_interest': []
}


class Stocks:

    def cryptoPrices(self):

        crypto_url = "https://finance.yahoo.com/cryptocurrencies?count=100&offset=0"
        crypto_page = requests.get(crypto_url)
        crypto_data = crypto_page.text
        soup = BeautifulSoup(crypto_data)

        for info in soup.find_all('div', {'class': 'Pos(r)'}):
            for name in info.find_all('td', {'class': 'Va(m) Ta(start) Px(10px) Fz(s)'}):
                if (len(CRYPO['name']) <= 24):
                    CRYPO['name'].append(name.text)
                else:
                    break
            for price in info.find_all('td', {'aria-label': 'Price (Intraday)'}):
                if (len(CRYPO['price']) <= 24):
                    CRYPO['price'].append(price.text)
                else:
                    break
            for change in soup.find_all('td', {'aria-label': 'Change'}):
                if (len(CRYPO['change']) <= 24):
                    CRYPO['change'].append(change.text)
                else:
                    break
            for chnage_percent in soup.find_all('td', {'aria-label': '% Change'}):
                if (len(CRYPO['percent_change']) <= 24):
                    CRYPO['percent_change'].append(chnage_percent.text)
                else:
                    break
            for cap in soup.find_all('td', {'aria-label': 'Market Cap'}):
                if (len(CRYPO['market_cap']) <= 24):
                    CRYPO['market_cap'].append(cap.text)
                else:
                    break
            for volume in soup.find_all('td', {'aria-label': 'Volume in Currency (Since 0:00 UTC)'}):
                if (len(CRYPO['volume_in_currency']) <= 24):
                    CRYPO['volume_in_currency'].append(volume.text)
                else:
                    break
            for supplies in soup.find_all('td', {'aria-label': 'Circulating Supply'}):
                if (len(CRYPO['circulating_supplies']) <= 24):
                    CRYPO['circulating_supplies'].append(supplies.text)
                else:
                    break

        crypto_df = pd.DataFrame({'Names': CRYPO['name'], 'Price': CRYPO['price'], 'Change': CRYPO['change'],
                                  'Percent Change': CRYPO['percent_change'], 'Market Cap': CRYPO['market_cap'],
                                  "Volume In Currency": CRYPO['volume_in_currency'],
                                  'Circulating Supplies': CRYPO['circulating_supplies']})
        return crypto_df

    def currencies(self):
        currency_url = "https://finance.yahoo.com/currencies"
        currency_page = requests.get(currency_url)
        currency_data = currency_page.text
        soup = BeautifulSoup(currency_data, 'html.parser')

        for listing in soup.find_all('div', {
            'class': 'Pos(r) Maw($newGridWidth) Miw(a)!--tab768 Miw(a)!--tab1024 Miw(a)!--mobp Miw(a)!--mobl Miw(a)!--mobxl Bxz(bb) Bdstartc(t) Bdstartw(20px) Bdendc(t) Bdends(s) Bdstarts(s) Bxz(bb) Mx(a) Mb(40px)'}):
            for find_name in listing.find_all('td', {'class': 'data-col1 Ta(start) Pend(10px)'}):
                CURRENCY['names'].append(find_name.text)
            for find_last_price in listing.find_all('td', {'class': 'data-col2 Ta(end) Pstart(20px)'}):
                CURRENCY['last_price'].append(find_last_price.text)
            for change in listing.find_all('td', {'class': 'data-col3 Ta(end) Pstart(20px)'}):
                CURRENCY['change'].append(change.text)
            for percent in listing.find_all('td', {'class': 'data-col4 Ta(end) Pstart(20px)'}):
                CURRENCY['percent_change'].append(percent.text)

        currency_df = pd.DataFrame(
            {'Names': CURRENCY['names'], 'Last Price': CURRENCY['last_price'], 'Change': CURRENCY['change'],
             'Change Percent': CURRENCY['percent_change']})
        print(currency_df)

    def mostActive(self):
        active_url = "https://finance.yahoo.com/most-active"
        active_page = requests.get(active_url)
        active_data = active_page.text
        soup = BeautifulSoup(active_data, 'html.parser')

        for listing in soup.find_all('table', {'class': 'W(100%)'}):
            for name in listing.find_all('td', {'aria-label': 'Name'}):
                MOST_ACTIVE['name'].append(name.text)
            for price in listing.find_all('td', {'aria-label': 'Price (Intraday)'}):
                MOST_ACTIVE['price'].append(price.text)
            for change in listing.find_all('td', {'aria-label': 'Change'}):
                MOST_ACTIVE['change'].append(change.text)
            for percent_change in listing.find_all('td', {'aria-label': '% Change'}):
                MOST_ACTIVE['percent_change'].append(percent_change.text)
            for volume in listing.find_all('td', {'aria-label': 'Volume'}):
                MOST_ACTIVE['volume'].append(volume.text)
            for avg_volume in listing.find_all('td', {'aria-label': 'Avg Vol (3 month)'}):
                MOST_ACTIVE['avg_volume'].append(avg_volume.text)
            for market_cap in listing.find_all('td', {'aria-label': 'Market Cap'}):
                MOST_ACTIVE['market_cap'].append(market_cap.text)

        mostActive_df = pd.DataFrame(
            {'Names': MOST_ACTIVE['name'], 'Price': MOST_ACTIVE['price'], 'Change': MOST_ACTIVE['change'],
             'Percent Change' : MOST_ACTIVE['percent_change'],
             'Volume': MOST_ACTIVE['volume'], 'Average Volume': MOST_ACTIVE['avg_volume'],
             'Market Cap': MOST_ACTIVE['market_cap']})
        mostActive_df['Names'] = mostActive_df['Names'].astype('str')
        mostActive_df['Price'] = mostActive_df['Price'].astype('float64')
        # mostActive_df['Percent Change'] = mostActive_df['Percent Change'].astype('float64')
        # mostActive_df['Volume'] = mostActive_df['Volume'].astype('float64')
        # mostActive_df['Average Volume'] = mostActive_df['Average Volume'].astype('float64')
        mostActive_df['Change'] = mostActive_df['Change'].astype('float64')

        print(len(MOST_ACTIVE['name']))
        print(len(MOST_ACTIVE['price']))
        print(len(MOST_ACTIVE['change']))
        print(len(MOST_ACTIVE['percent_change']))
        print(len(MOST_ACTIVE['volume']))
        print(len(MOST_ACTIVE['avg_volume']))
        print(len(MOST_ACTIVE['market_cap']))
        date = dt.datetime.today().strftime("%m/%d/%Y")
        mostActive_df['UploadDate'] = date
        mostActive_df.to_csv('active.csv', header=True, index= False, mode='w')

        pd.set_option('display.max_columns', None)
        print(mostActive_df.loc[mostActive_df['Names'] == 'TripAdvisor, Inc.'])



        # best_investment = mostActive_df.loc[mostActive_df['Change'].idxmax()]['Names']
        # print(best_investment)
        # mostActive_df.to_csv('active.csv', mode='a', header=False)


    def commodities(self):
        commodity_url = "https://finance.yahoo.com/commodities"
        commodity_page = requests.get(commodity_url)
        commodity_data = commodity_page.text
        soup = BeautifulSoup(commodity_data, 'html.parser')

        for listing in soup.find_all('div', {'class': 'Ovx(a)'}):
            for name in listing.find_all('td', {'class': 'data-col1 Ta(start) Pend(10px)'}):
                COMMODITIES['name'].append(name.text)
            for last_price in listing.find_all('td', {'class': 'data-col2 Ta(end) Pstart(20px)'}):
                COMMODITIES['last_price'].append(last_price.text)
            for market_time in listing.find_all('td', {'class': 'data-col3 Ta(end) Pstart(20px)'}):
                COMMODITIES['market_time'].append(market_time.text)
            for change in listing.find_all('td', {'class': 'data-col4 Ta(end) Pstart(20px)'}):
                COMMODITIES['change'].append(change.text)
            for percent_change in listing.find_all('td', {'class': 'data-col5 Ta(end) Pstart(20px)'}):
                COMMODITIES['percent_change'].append(percent_change.text)
            for volume in listing.find_all('td', {'class': 'data-col6 Ta(end) Pstart(20px)'}):
                COMMODITIES['volume'].append(volume.text)
            for open_interest in listing.find_all('td',
                                                  {'class': 'data-col7 Ta(end) Pstart(20px) Pend(10px) W(120px)'}):
                COMMODITIES['open_interest'].append(open_interest.text)

        print(len(COMMODITIES['name']))
        print(len(COMMODITIES['last_price']))
        print(len(COMMODITIES['market_time']))
        print(len(COMMODITIES['change']))
        print(len(COMMODITIES['percent_change']))
        print(len(COMMODITIES['volume']))
        print(len(COMMODITIES['open_interest']))

        commodity_df = pd.DataFrame({'Name': COMMODITIES['name'], 'Last Price': COMMODITIES['last_price'],
                                     'Market Time': COMMODITIES['market_time'], 'Change': COMMODITIES['change'],
                                     'Percent Change': COMMODITIES['percent_change'],
                                     'Volume': COMMODITIES['volume'], 'Open Interest': COMMODITIES['open_interest']})


if __name__ == '__main__':
    zoinks = Stocks()
    zoinks.mostActive()
