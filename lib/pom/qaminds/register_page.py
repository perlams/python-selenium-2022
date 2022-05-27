from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage
from random import randint


class RegisterPage(BasePage):
    # Locators
    _firstNameField = (By.ID, "input-firstname")
    _LastNameField = (By.ID, "input-lastname")
    _emailField = (By.ID, "input-email")
    _phoneField = (By.ID, "input-telephone")
    _passwordField = (By.ID, "input-password")
    _passwordConfirmField = (By.ID, "input-confirm")
    _privacyPolicyCheckBox = (By.XPATH, "//input[@name='agree']")
    _continueBtn = (By.CLASS_NAME, "btn-primary")
    _alert = (By.CLASS_NAME, "alert-danger")
    _errorMsgFirstName = (By.XPATH, "//input[@id='input-firstname']/following-sibling::div")
    _errorMsgLastName = (By.XPATH, "//input[@id='input-lastname']/following-sibling::div")
    _errorMsgEmail = (By.XPATH, "//input[@id='input-email']/following-sibling::div")
    _errorMsgPhone = (By.XPATH, "//input[@id='input-telephone']/following-sibling::div")
    _errorMsgPassword = (By.XPATH, "//input[@id='input-password']/following-sibling::div")
    _successfulRegisterMsg =(By.TAG_NAME, "h1")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_medium())
        super().__init__(driver, wait)

    def complete_form_valid_values(self, first_name: str, last_name: str, phone: str, password: str,
                                   confirm_password: str):

        email = "qa"+str(randint(0, 100000))+"@minds.com"
        print("email:", email)
        self._write(self._firstNameField, first_name)
        self._write(self._LastNameField, last_name)
        self._write(self._emailField, email)
        self._write(self._phoneField, phone)
        self._write(self._passwordField, password)
        self._write(self._passwordConfirmField, confirm_password)
        self._click(self._privacyPolicyCheckBox)
        self._click(self._continueBtn)
        self._get_element(self._successfulRegisterMsg).is_displayed()
        return self._get_element(self._successfulRegisterMsg).text

    def submit_an_incomplete_form(self):
        self._click(self._continueBtn)
        self._get_element(self._alert).is_displayed()

    def get_first_name_error(self):
        self._get_element(self._errorMsgFirstName).is_displayed()
        actual_first_name_error = self._get_element(self._errorMsgFirstName).text
        return actual_first_name_error

    def get_last_name_error(self):
        self._get_element(self._errorMsgLastName).is_displayed()
        actual_last_name_error = self._get_element(self._errorMsgLastName).text
        return actual_last_name_error

    def get_email_error(self):
        self._get_element(self._errorMsgEmail).is_displayed()
        actual_email_error = self._get_element(self._errorMsgEmail).text
        return actual_email_error

    def get_phone_error (self):
        self._get_element(self._errorMsgPhone).is_displayed()
        actual_phone_error = self._get_element(self._errorMsgPhone).text
        return actual_phone_error

    def get_password_error(self):
        self._get_element(self._errorMsgPassword).is_displayed()
        actual_password_error = self._get_element(self._errorMsgPassword).text
        return actual_password_error




