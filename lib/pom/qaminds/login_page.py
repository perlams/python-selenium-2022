from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class LoginPage(BasePage):

    # Locators
    _emailField = (By.ID, "input-email")
    _passwordField = (By.ID, "input-password")
    _forgot_password = (By.LINK_TEXT, "Forgotten Password")
    _loginBtn = (By.XPATH, "//input[@value ='Login']")
    _continueBtn = (By.LINK_TEXT, "Continue")
    _alert = (By.CLASS_NAME, 'alert-danger')

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def login(self, email: str, password: str):
        self._write(self._emailField, email)
        self._write(self._passwordField, password)
        self._click(self._loginBtn)

    def forgotten_password(self):
        self._click(self._forgot_password)

    def select_menu(self, menu_name: str):
        """Select top menu option.

        :param menu_name: Menu display name.
        :return: None.
        """
        loc = (By.PARTIAL_LINK_TEXT, menu_name)
        self._click(loc)

    def continue_as_new_customer(self):
        self._click(self._continueBtn)

    def is_login_warn_displayed(self):
        return self._get_element(self._alert).is_displayed()
