import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_driver_path = '../drivers/chromedriver'
gecko_driver_path = '../drivers/geckodriver'

url = 'https://qamindslab.com'
#service = Service(chrome_driver_path)
service = Service(gecko_driver_path )

#driver = webdriver.Chrome(service=service)
driver = webdriver.Firefox(service=service)
driver.get(url)
time.sleep(3)
driver.quit()