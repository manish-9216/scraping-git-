from sqlite3 import DataError
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
import string

chrome_options = webdriver.ChromeOptions()

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)
driver.maximize_window()



# for i in alphabet:
driver.get('https://www.prokerala.com/kids/baby-names/boy/.html')
   
time.sleep(10)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
    
   
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
       
   
# element = driver.find_element_by_xpath("//*[@id='root']/div/main/div[3]/div/div/div[2]")

# a=1
# while a==1:
#     driver.execute_script("arguments[0].scrollBy(0, 500)", element)
#     time.sleep(2)
    
#     i=0
    
    
    
    
    
#     try:
         
#         for d in soup.find_all('div',  class_="listing_container"):
#             title = d.find_all('div', class_="baby-name M15_42" )
#             for i in title:
#                 data=i.text
#                 if data in test:
#                     print('dublicate removed')
#                 else:
#                     test.append(data)
#         print(len(test))
#         if len(test)>=int(200):
#             break
                       
#     except:
#        break
    
    
   
            

# print(test)