
import sys
sys.path.append('D:/whitehat2/python_VSC/C127/venv/Lib/site-packages')

#sys.path.append('C:/Users/pbnaz/AppData/Local/Packages/PythonSoftwareFoundation.Python.3.10_qbz5n2kfra8p0/LocalCache/local-packages/Python310/site-packages')

from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv

START_URL ="https://exoplanets.nasa.gov/exoplanet-catalog/"
browser =webdriver.Chrome("D:/whitehat2/python_VSC/C127/chromedriver")
browser.get(START_URL)
time.sleep(10)

def scrape():
    headers = ["name","light_years_from_earth","planet_mass", "stellar_magnitude","discovery_date"]
    planet_data = []
    for i in range(0,428):
        soup =BeautifulSoup(browser.page_source,"html.parser")
        for ul_tag in soup.find_all("ul", attrs={"class","exoplanet"}):
            li_tags =ul_tag.find_all("li")
            temp_list = []
            for index, li_tag in enumerate(li_tags):
                if index == 0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])
                else:
                    try:
                        temp_list.append(li_tag.contents[0])
                    except:
                        temp_list.append("")
            planet_data.append(temp_list)
            
        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a').click()
    with open ("scraper_1.csv","w") as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(headers)
        csvwriter.writerows(planet_data)

scrape()


