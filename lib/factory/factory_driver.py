from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.firefox_driver import create_driver as create_firefox
from lib.factory.chrome_driver import create_driver as create_chrome
from lib.config import config


def get_driver() -> WebDriver:
    config.load_config()
    browser = config.get_browser_name()
    if browser.lower() == 'chrome':
        driver = create_chrome()
    elif browser.lower() == 'firefox':
        driver = create_firefox()
    else:
        raise ValueError(f'Invalid browser {browser}')

    if config.get_headless_mode():
        driver.set_window_size(**config.get_headless_resolution())
    else:
        driver.maximize_window()
    driver.set_page_load_timeout(config.get_page_load_timeout())
    driver.implicitly_wait(config.get_implicit_wait())
    return driver
