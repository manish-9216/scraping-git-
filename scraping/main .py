import requests
import selenium
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
 
from urllib.parse import urlparse
import urllib.request
import time

import itertools as it
 


# url = "https://parenting.firstcry.com/baby-names/" 
# driver.get(url)
# time.sleep(5)

 
# soup = BeautifulSoup(driver.page_source, 'html.parser')
# alpha_list = []
# search = soup.find_all('div', class_="alphabet_list")
# # print(search)
# try:
#     s = soup.find_all('li', class_="left alphabets M16_white")
#     for i in s:
#         b = 'https://parenting.firstcry.com/baby-names/starting-with/{}/.format(i)'
#         parsed_uri = urlparse(b)
#         alpha_list.append()
      
# except:
#     pass
names = []
main_url_list = []   
myList = [chr(chNum) for chNum in list(range(ord('a'),ord('z')+1))]

for i in myList:
    url = "https://parenting.firstcry.com/baby-names/starting-with/{}/".format(i)
    main_url_list.append(url)


for url in main_url_list:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    driver.get(url)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')

    # aa = soup.find_all('div',  class_="listing_container")
    # for i  in aa:
    #     print(i.find_all('li').find('div', class_='baby-name M15_42'))

    #     # title = soup.find_all('ul', class_="names-list" )
    #     # for i in title:
    #     #     i.find('')



    for d in soup.find_all('div',  class_="listing_container"):
            title = d.find_all('div', class_="baby-name M15_42" )
             
            for i in title:
                # element = driver.find_element_by_class_name("listing_container")

                # actions = ActionChains(driver)
                # actions.move_to_element(element).perform()
                # while True:
                #     element = driver.find_element_by_xpath("/html/body/div[1]/div/main/div[3]/div/div/div[2]")
                #     driver.execute_script("arguments[0].scrollIntoView(true);", element);

                #     time.sleep(3)
                print(i.text)