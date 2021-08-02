# Webscraping using python
First, let's start by defining the term web scraping 
###### What is web scraping ? 
Web scraping is the process of executing an algorithm that aims to extract important data. The amount of scrapped data could be huge so that we can use it for future analysis. For example, if we are scrapping an online site that sold certain items, we can use the scrapped data to analyse the future trends, to understand customers'behavior during different periods, to discover reasons behind the bestseller product  

In this project, I will show you how to scrape or to extract useful information about wine bottles and how we could use the amount of extracted data for future analysis using machine learning algorithms. 
The web site that we are going to scrape is the next : https://www.winemag.com/?s=&drink_type=wine&page=1 
Actually, only some pages are going to be scraped then all the scrapped data will be transformed into a dataframe and in the final stage, will be saved in a csv file. 
The obtained csv file has the next format : 


###### Requirements: 
In order to run this project correctly you will need to satisfy the next requirements 
- Python: version '3.7'
- Selenium : version '3.141.0
- Numpy : version '1.19.1' 
- Pandas : version '1.1.0'
- Webdriver manager for chrome: chromeDriverManager 
