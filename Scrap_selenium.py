from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import json
import numpy as np
import time
import pandas as pd


# Define the list of variables to be used
scrape_data = []
my_dataset={}
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")

class ReviewFormatException(Exception):
    """Exception when the format of a review page is not understood by the scraper"""

    def __init__(self, message):
        self.message = message
        super(Exception, self).__init__(message)

def scrape_Page(url):# To get all attribute existing in one page of site
    driver_review =webdriver.Chrome(ChromeDriverManager().install(), options=options)
    driver_review.get(url)
    try:
        return driver_review
    except ReviewFormatException as e:
        print(f"\n-----\nError parsing: {review_url}\n{e.message}\n-----")


def scrape_items_review (driver_review):# here to get all the data fields from one review url
        mydict={}
        try:
            # getting the description
            description_elements = driver_review.find_element_by_class_name("description")
            description = description_elements.text
            mydict['Description']=description

            # getting the rating
            rates = driver_review.find_element_by_class_name("rating")
            point = rates.text
            mydict['Points'] = point.split('\n')[0]


            # getting the title
            tit = driver_review.find_element_by_class_name("article-title")
            title = tit.text
            mydict['Title'] = title.split('\n')[2]


            # getting the price, winery, country, variety, designation : The primary information
            primary_information = driver_review.find_element_by_class_name("primary-info")
            prim_info = primary_information.text
            split_prim_info = prim_info.split('\n')

            price = split_prim_info[1]
            mydict['Price'] = price.split(',')[0]
            if len(split_prim_info) == 10:
                designation = split_prim_info[3]
                variety = split_prim_info[5]
                appellation = split_prim_info[7]
                winery = split_prim_info[9]
            if len(split_prim_info) == 8:
                designation = np.nan
                variety = split_prim_info[3]
                appellation = split_prim_info[5]
                winery = split_prim_info[7]
            mydict['Designation'] = designation
            mydict['Variety'] = variety
            mydict['Country'] = appellation
            mydict['Winery'] = winery

            # getting the taster name
            name = driver_review.find_element_by_class_name("taster-area")
            taster_name = name.text
            mydict['Taster'] = taster_name

            # getting the price, winery, country, variety, designation : The primary information
            secondary_information = driver_review.find_element_by_class_name("secondary-info")
            sec_info = secondary_information.text

            split_second_info = sec_info.split('\n')
            alcohol = split_second_info[1]
            mydict['Alcohol'] = alcohol

            bottle_size = split_second_info[3]
            mydict['Bottle size']= bottle_size

            category = split_second_info[5]
            mydict['Category'] = category
            if len(split_second_info) == 10:
                importer = np.nan
                mydict['Importer'] = importer
                date_published = split_second_info[7]
                mydict['Date published'] = date_published

            if len(split_second_info) == 12:
                importer = split_second_info[7]
                mydict['Importer'] = importer
                date_published = split_second_info[9]
                mydict['Date published'] = date_published
            return mydict
        except Exception as e:
            print("Encountered error", e)



colum = ['Description', 'Points', 'Title', 'Price', 'Designation', 'Variety', 'Country', 'Winery', 'Taster', 'Alcohol',
        'Bottle size', 'Category', 'Importer', 'Date published']


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.winemag.com/?s=&drink_type=wine&region=Piedmont&pub_date_web={1}&page=300")

# print(driver.page_source)
# driver.quit()
page = 301   ###

DATASET = pd.DataFrame(columns=colum)
while True:
    time.sleep(7)
    # Locating elements by path
    reviews = driver.find_elements_by_xpath("/html/body/div[2]/div/section/section/div/div/section/div[1]/div/div/div[2]/ul/li")

    for review in reviews:
        # isolated_review_count += 1
        items = review.find_elements_by_tag_name("a")
        for item in items:
            review_url = item.get_attribute('href')
            # print (review_url)
            scrape_data.append(review_url)
            review_data = scrape_Page(review_url)
            my_dataset = scrape_items_review(review_data)

            my_dataset=pd.DataFrame([my_dataset.values()], columns=colum)
            DATASET = pd.concat([DATASET, my_dataset], axis=0, ignore_index=True)
    if len(driver.find_elements_by_css_selector("#next-page")) > 0:
        print(page)
        url = "https://www.winemag.com/?s=&drink_type=wine&region=Piedmont&pub_date_web={1}&page="+str(page)
        driver.get(url)

        # It will traverse for only 5 pages as you are after if want more page just comment the below if block
        if int(page) > 321:  # Istopped here because I saw that it is the old page
            print('end')
            break

        page += 1
    else:
        break

# Write your csv file :

DATASET.to_csv('Piemont_data250-280..', index=False, header=False, sep=';', encoding='utf-8')

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

import pandas as pd

driver = webdriver.Chrome()
driver_review.get(
    'https://finance.detik.com/berita-ekonomi-bisnis/d-5307853/ri-disebut-punya-risiko-korupsi-yang-tinggi?_ga=2.13736693.357978333.1608782559-293324864.1608782559')

userid_element = driver_review.find_elements_by_xpath('//*[@id="cmt66364625"]/div[1]/div[1]/text()')
userid = userid_element.text
