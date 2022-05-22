from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class HomePage(BasePage):

    _logo = (By.ID, 'logo')
    _input_search = (By.NAME, 'search')
    _button_search = (By.XPATH, "//div[@id='search']//button")
    _cart_total = (By.ID, 'cart-total')
    _currency = (By.XPATH, "//*[@id='form-currency']//strong")
    _currency_dropdown = (By.XPATH, "//*[@id='form-currency']//button[@data-toggle]")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def is_logo_visible(self) -> bool:
        """Get logo status.

        :return: True if logo is visible, otherwise False.
        """
        return self._get_element(self._logo).is_displayed()

    def search(self, text: str):
        """Search product.

        :param text: Product name.
        :return: None
        """
        self._write(self._input_search, text)
        self._click(self._button_search)

    def select_menu(self, menu_name: str):
        """Select top menu option.

        :param menu_name: Menu display name.
        :return: None.
        """
        loc = (By.PARTIAL_LINK_TEXT, menu_name)
        self._click(loc)

    def select_sub_menu(self, main_menu_name: str, sub_menu_name: str):
        """Select sub menu option.

        :param main_menu_name: Main menu option.
        :param sub_menu_name: Sub menu option.
        :return: None
        """
        self.select_menu(main_menu_name)
        self.select_menu(sub_menu_name)

    def get_cart_total(self) -> str:
        """Get cart total.

        :return: Cart total.
        """
        return self._get_text(self._cart_total)

    def get_currency(self) -> str:
        """Get currency.

        :return: Currency symbol
        """
        return self._get_text(self._currency)

    def set_currency(self, name: str):
        """Set currency.

        :param name: Valid options: EUR, GBP and USD.
        :return:None
        """
        self._click(self._currency_dropdown)
        if name not in ['USD', 'GBP', 'EUR']:
            raise ValueError(f'Invalid currency: {name}')
        loc = (By.XPATH, f"//*[@id='form-currency']//button[@name='{name}']")
        self._click(loc)

    def select_product(self, name: str):
        """Select product by name

        :param name: Product display name.
        :return: None
        """
        loc = (By.LINK_TEXT, name)
        self._click(loc)