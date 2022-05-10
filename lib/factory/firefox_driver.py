from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver


def create_driver() -> WebDriver:
    driver_path = '../../../drivers/geckodriver'
    service = Service(driver_path)
    return webdriver.Firefox(service=service)

