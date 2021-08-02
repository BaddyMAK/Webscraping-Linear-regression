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


As environment, we will use PyCharm, to scrape the web site and to extract the required data while we will use Jupyter notebook to apply a machine learning algorithm that we will specify later. 

# Site description 

The data was scraped from the site https://www.winemag.com/?s=&drink_type=wine&page=1 during the week of August 2nd, 2020. As you notice, this site is composed by almost 7000 principal pages where each of those pages, has at most six other secondary / sub-pages. If you open any secondary page you will find that it contains the next information that we want to extract : 
- Title : The review title 
- Rating/ Points : The number of points WineEnthusiast rated the wine on a scale of 1-100 (though they say they only post reviews for
- Price : The cost for a bottle of the wine
- Designation : The vineyard within the winery where the grapes that made the wine are from
- Variety 
- Appellation : The country that the wine is from
- Winery : The type of grape used to make a wine
- Alchol : The alchol percentage
- Bottle size : Dimensions of the bottle 
- Importer : The person or the firm that has import this product
- Date Published : The date when the review was published
- User AVG Rating 

In the Scrap_selenium.py file you will find a simplified code or algorithm that allows you to scrape the site. You can specify how many pages do you want to scrape.

As you see from the next example, https://www.winemag.com/buying-guide/disznoko-2007-eszencia-tokaji/ the dispayed information are splitted into two types : 
- Primary information : Price, Winery, Country, Variety, Designation
- Secondary information : Alcohol, Bottle size, Category, Importer, Date published
