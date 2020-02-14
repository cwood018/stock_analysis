import pandas as pd
from bs4 import BeautifulSoup
import requests
import datetime as dt
import stocks



class Analysis:

    def setDataFrame(self):

        zoinks = pd.read_csv('active.csv', index_col= 0)
        pd.set_option('display.max_columns', None)
        print(zoinks.loc[zoinks['Names'] == 'Ford Motor Company'])





if __name__ == '__main__':
    ana = Analysis()
    ana.setDataFrame()