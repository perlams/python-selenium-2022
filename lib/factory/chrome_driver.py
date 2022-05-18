from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from lib.config import config

__INCOGNITO = '--incognito'
__HEADLESS = '--hedless'



def create_driver() -> WebDriver:
    chrome_options = webdriver.ChromeOptions()
    if config.get_incognito_mode():
        chrome_options.add_argument(__INCOGNITO)
    if config.get_headless_mode():
        chrome_options.add_argument(__HEADLESS)
    service = Service(config.get_driver_path())
    print(f'HEADLESS: {chrome_options.headless}')
    return webdriver.Chrome(service=service, options=chrome_options)

