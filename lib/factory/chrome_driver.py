from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver


def create_driver() -> WebDriver:
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--incognito')
    chrome_options.add_argument('--headless')
    driver_path = '../../../drivers/chromedriver'
    service = Service(driver_path)
    print(f'HEADLESS: {chrome_options.headless}')
    return webdriver.Chrome(service=service, options=chrome_options)

