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


info=[]

# for z in range(1,(20+1)):
    
#     if z==1:
driver.get('https://www.prokerala.com/kids/baby-names/boy/')

soup = BeautifulSoup(driver.page_source, 'html.parser')

search = soup.find_all('table', class_="table name-list-wrapper")     

for d in search:
    
    link = d.find_all('a' )
    for i in link:
           x=(i.get('href'))
           info.append(x)

print(info)

# info.remove('/kids/baby-names/hindu-boy-names.html')
# info.remove('/kids/baby-names/popular-christian-boy-names.html')


   
for i in info:
    driver.get('https://www.prokerala.com'+str(i))


## for names list------------------------------------------------------------

   
    # for z in range(1,(20+1)):
    
    #     if z==1:

    #     time.sleep(10)
        
    # else:
    #     driver.get('https://www.prokerala.com/kids/baby-names/boy/page-'+str(z)+'.html')   
    #     time.sleep(10)
    
   


    # x=driver.find_elements_by_xpath('//*[@id="wrapper"]/main/div/table')

    # for i in range(1,(len(x)+1)):
        
    #     y=driver.find_elements_by_xpath('//*[@id="wrapper"]/main/div/table['+str(i)+']'+'/tbody/tr')
        
    #     for count in range(1,(len(y)+1)):
            
    #         try:
    #             data=driver.find_element_by_xpath('//*[@id="wrapper"]/main/div/table['+str(i)+']'+'/tbody/tr['+str(count)+']'+'/td[1]/span/a').text
            
    #             info.append(data)

    #         except:
    #             print('item'+str(count)+'skipped')
    #             continue
            
    # print(info)   

## for names list------------------------------------------------------------



