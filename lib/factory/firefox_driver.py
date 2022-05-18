from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.remote.webdriver import WebDriver
from lib.config import config

__FIREFOX_PRIVATE = 'browser.privatebrowsing.autostart'

def create_driver() -> WebDriver:
    ff_options = webdriver.FirefoxOptions()
    ff_profile = webdriver.FirefoxProfile()
    ff_profile.set_preference(__FIREFOX_PRIVATE, config.get_incognito_mode())
    ff_options.headless = config.get_headless_mode()
    service = Service(config.get_driver_path())
    return webdriver.Firefox(service=service, options=ff_options, firefox_profile=ff_profile)

