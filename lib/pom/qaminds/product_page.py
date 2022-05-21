from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage

class ProductPage(BasePage):

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def get_name(self):
      pass

    def get_price(self):
      pass

    def get_ex_tax(self):
      pass

    def get_product_code(self):
      pass

    def get_availability(self):
      pass

    def get_description(self):
      pass

    def add_to_cart(self):
      pass

    def get_total_reviews(self):
      pass