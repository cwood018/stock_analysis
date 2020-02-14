# stock_analysis

Python Web Scraper to scrape from the top Yahoo Finance tables, such as Most Active, Commodities, Cryptcurrencies and Currencies. With this data collected daily, we can visualize the stock market as well possibly use machine learning to predict trends within the stock market. 

# To - Do

Create a Lamda Function to collect data daily and insert into a AWS RDS table

Create a React Application to show the visualization on the site 

# Completed 

Web Scraping to DataFrame is completed for all categories

Found a way to isolate the company names with different dates without buying RDS table by simply putting DataFrames for different days in the same CSV file and attaching it to another CSV.
