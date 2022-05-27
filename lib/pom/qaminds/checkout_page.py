from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage


class CheckoutPage(BasePage):
    _emailField = (By.ID, "input-email")
    _passwordField = (By.ID, "input-password")
    _loginBtn = (By.ID, "button-login")
    _errorMessage = (By.CLASS_NAME, "alert-danger")
    _checkoutTitle = (By.TAG_NAME, "h1")
    _forgot_password = (By.LINK_TEXT, "Forgotten Password")
    _forgottenTitle = (By.TAG_NAME, "h1")
    _registerCheck = (By.XPATH, "//*[@value='register']")
    _guestCheck = (By.XPATH, "//*[@value='guest']")
    _continueBtn = (By.ID, "button-account")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def login_with_invalid_credentials(self, email: str, password: str):
        self._write(self._emailField, email)
        self._write(self._passwordField, password)
        self._click(self._loginBtn)
        self._get_element(self._errorMessage).is_displayed()
        return self._get_element(self._errorMessage).text

    def login_with_valid_credentials(self, email: str, password: str):
        self._write(self._emailField, email)
        self._write(self._passwordField, password)
        self._click(self._loginBtn)
        self._get_element(self._checkoutTitle).is_displayed()
        return self._get_element(self._checkoutTitle).text

    def forgotten_password(self):
        self._click(self._forgot_password)
        self._get_element(self._forgottenTitle).is_displayed()
        return self._get_element(self._forgottenTitle).text