url = "https://my.uq.edu.au/programs-courses/requirements/plan/DAOPRC2460/2022"

from time import sleep
from selenium import webdriver

options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')

driver = webdriver.Chrome(options=options) 
driver.get(url)

print("start sleep")
sleep(1)

source = driver.page_source
print(source)