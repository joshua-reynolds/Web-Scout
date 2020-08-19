from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import bs4 as bs
from notify_run import Notify
import webbrowser

"""
Amazon checks for bots, so chromedriver is required to access the page text
RepFitness is less guarded so only urllib is required
"""

#====================================
# Powerblock Compact Stand (Amazon)
#====================================

# get the path of ChromeDriverServer
dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"

# make the browser window invisible
options = Options()
options.headless = True

# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)

# Let the driver try to find the content for 10 seconds
driver.implicitly_wait(10)

# powerblock amazon url 
url='https://www.amazon.com/POWERBLOCK-Compact-Weight-Stand-Black/dp/B01A9981M0/ref=sr_1_1?crid=1F57GF306BHXP&dchild=1&keywords=powerblock+compact+weight+stand&qid=1597100715&sprefix=powerblock+com%2Caps%2C203&sr=8-1'

## test url
#url2 = 'https://www.amazon.com/Ghost-Tsushima-PlayStation-4/dp/B08BSKT43L/ref=zg_bsnr_videogames_home_1?_encoding=UTF8&psc=1&refRID=1Y7M1E00G5NXSZJ0X6R4'

# get the page text
driver.get(url)
html = driver.page_source
soup = bs.BeautifulSoup(html, 'lxml')
amz_price = soup.find(id='priceblock_ourprice')

# get current time
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M")

# intialize notify
notify = Notify() 

# if price tag has a value send the notification
if amz_price:
    print('Powerblock LCS is available {}!'.format(dt_string))
    notify.send('Powerblock LCS is available {}!'.format(dt_string))
    webbrowser.open(url)
else:
    print('Powerblock LCS is not available {}!'.format(dt_string))
    #notify.send('Powerblock LCS is not available {}!'.format(dt_string))
    
# close the browser window
driver.quit()

#=====================
# REP AB 3000
#=====================

# open the url
source = urllib.request.urlopen('https://www.repfitness.com/strength-equipment/strength-training/benches/rep-ab3000-fid-adj-bench').read()

#get the soup
soup = bs.BeautifulSoup(source,'lxml')
availability = soup.findAll("p", class_="availability out-of-stock")

# intialize notify
notify = Notify() 

# get current time
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M")

# Check if availability tag object has length greater than 0
if len(availability) > 0:
    print('AB-3000 is not available {}'.format(dt_string))
    #notify.send('AB-3000 is not available {}'.format(dt_string))    
    
else:
    # send alert
    print('AB-3000 is available {}'.format(dt_string))
    notify.send('AB-3000 is available {}!'.format(dt_string))  

#=====================
# REP AB 3100
#=====================

# open the url
source = urllib.request.urlopen('https://www.repfitness.com/strength-equipment/strength-training/benches/rep-ab-3100-fi-bench').read()

#get the soup
soup = bs.BeautifulSoup(source,'lxml')
availability = soup.findAll("p", class_="availability out-of-stock")

# intialize notify
notify = Notify() 

# get current time
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M")

# Check if availability tag object has length greater than 0
if len(availability) > 0:
    print('AB-3100 is not available {}'.format(dt_string))
    #notify.send('AB-3100 is not available {}'.format(dt_string))    
    
else:
    # send alert
    print('AB-3100 is available {}!'.format(dt_string))
    notify.send('AB-3100 is available {}!'.format(dt_string))  


#=====================
# REP AB 5000
#=====================

# open the url
source = urllib.request.urlopen('https://www.repfitness.com/strength-equipment/strength-training/benches/rep-ab-5000').read()

#get the soup
soup = bs.BeautifulSoup(source,'lxml')
availability = soup.findAll("p", class_="availability out-of-stock")

# intialize notify
notify = Notify()

# get current time
now = datetime.now()
dt_string = now.strftime("%m/%d/%Y %H:%M")

# Check if availability tag object has length greater than 0
if len(availability) > 0:
    print('AB-5000 is not available {}'.format(dt_string))
    #notify.send('AB-5000 is not available {}'.format(dt_string))    
    
else:
    # send alert
    print('AB-5000 is available {}!'.format(dt_string))
    notify.send('AB-5000 is available {}!'.format(dt_string))  