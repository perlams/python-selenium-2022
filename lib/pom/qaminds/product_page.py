from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from lib.config import config
from lib.pom.common.base_page import BasePage


class ProductPage(BasePage):
    _product_name_loc = (By.XPATH, ' //*[@id="content"]//h1')
    _product_price_loc = (By.XPATH, ' //*[@id="content"]//h2')
    _ex_tax_loc = (By.XPATH, ' //*[@id="content"]/div/div[2]/ul[2]/li[2]')
    _product_code_loc = (By.XPATH, "//*[@id='content']/div/div[2]/ul[1]/li[1]")
    _prod_availability_loc = (By.XPATH, "//*[@id='content']/div/div[2]/ul[1]/li[2]")
    _prod_description_loc = (By.XPATH, "//*[@id='tab-description']/div")
    _add_to_cart_button_loc = (By.ID, "button-cart")
    _prod_reviews_loc = (By.XPATH, "//*[@id='content']//p/a[1]")
    _alert_loc = (By.CLASS_NAME, "alert-success")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def get_name(self):
        prod_name: WebElement = self.wait.until(EC.visibility_of_element_located(self._product_name_loc))
        return prod_name.text

    def get_price(self):
        prod_price: WebElement = self.wait.until(EC.visibility_of_element_located(self._product_price_loc))
        return prod_price.text

    def get_ex_tax(self):
        ex_tax: WebElement = self.wait.until(EC.visibility_of_element_located(self._ex_tax_loc))
        return ex_tax.text

    def get_product_code(self):
        prod_code: WebElement = self.wait.until(EC.visibility_of_element_located(self._product_code_loc))
        return prod_code.text

    def get_availability(self):
        prod_availability: WebElement = self.wait.until(EC.visibility_of_element_located(self._prod_availability_loc))
        return prod_availability.text

    def get_description(self):
        return self._get_element(self._prod_description_loc).is_displayed()

    def add_to_cart(self):
        self._click(self._add_to_cart_button_loc)

    def is_login_warn_displayed(self):
        return self._get_element(self._alert_loc).is_displayed()

    def get_total_reviews(self):
        prod_reviews: WebElement = self.wait.until(EC.visibility_of_element_located(self._prod_reviews_loc))
        return prod_reviews.text[1:1]

