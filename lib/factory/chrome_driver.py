from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.remote.webdriver import WebDriver


def create_driver() -> WebDriver:
    driver_path = '../../../drivers/chromedriver'
    service = Service(driver_path)
    return webdriver.Chrome(service=service)

