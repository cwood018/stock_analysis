# Stock Analysis

Stock Analysis is python driven with BeautifulSoup along with Pandas to store the data in a dataframe. The scraping is done by scraping Yahoo Finance with tables that include Commodities, Currencies, Cryptocurrencies along with Most Active Stocks. This will be attached to a AWS Lambda to run the script daily and insert into a AWS RDS table to run analysis and pull from for data visualization of the stocks. Down the road once more historical data is gathered, machine learning can then be enforced to predict stock prices.

This is a side project and a fun passion project for myself. 

## To Do

Link to AWS Lambda function for daily scheduled scrape

Develop React Site to show visualization and latest numbers for users 

## Completed

Scraper is completely down for all tables on Yahoo Finance

Tested locally for data visualization for a few days written into a CSV File before table for testing
