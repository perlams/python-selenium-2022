from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.firefox_driver import create_driver as create_firefox
from lib.factory.chrome_driver import create_driver as create_chrome


def get_driver(browser: str) -> WebDriver:
    if browser.lower() == 'chrome':
        return create_chrome()
    elif browser.lower() == 'firefox':
        return create_firefox()
    else:
        raise ValueError(f'Invalid browser {browser}, supporter browsers: Firefox and Chrome')
