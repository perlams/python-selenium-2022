from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class ProductPage(BasePage):
    name = (By.XPATH, "//*[@id='content']//h1")
    price = (By.XPATH, "//*[@id='content']//li/h2")
    # TODO - Improve XPATH, remove text dependency
    ex_tax = (By.XPATH, "//li[contains(normalize-space(.), 'Ex Tax:')]")
    product_code = (By.XPATH, "//li[contains(normalize-space(.), 'Product Code:')]")
    availability = (By.XPATH, "//li[contains(normalize-space(.), 'Availability:')]")
    description = (By.XPATH, "//*[@id='tab-description']/div")
    add_to_cart_loc = (By.ID, "button-cart")
    reviews = (By.XPATH, "//*[@class='rating']//a[contains(normalize-space(.), 'reviews')]")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def get_name(self):
        return self._get_text(self.name)

    def get_price(self):
        return self._get_text(self.price)

    def get_ex_tax(self):
        return self._get_value_from_label(self.ex_tax)

    def get_product_code(self):
        return self._get_value_from_label(self.product_code)

    def get_availability(self):
        return self._get_value_from_label(self.availability)

    def get_description(self):
        return self._get_text(self.description)

    def add_to_cart(self):
        self._click(self.add_to_cart_loc)

    def get_total_reviews(self):
        return self._get_value_from_label(self.reviews, delimiter=None, value_index=0)

    def _get_value_from_label(self, locator: tuple, delimiter: str = ':', value_index: int = -1):
        value = self._get_text(locator)
        return value.split(delimiter)[value_index].lstrip()
