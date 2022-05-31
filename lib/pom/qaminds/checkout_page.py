import time
from random import randint

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from lib.config import config
from lib.pom.common.base_page import BasePage
from selenium.webdriver.support.select import Select


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
    _guestRadio = (By.XPATH, "//*[@value='guest']")
    _first_name = (By.ID, "input-payment-firstname")
    _last_name = (By.ID, "input-payment-lastname")
    _address1 = (By.ID, "input-payment-address-1")
    _emailPayment = (By.ID, "input-payment-email")
    _phone = (By.ID, "input-payment-telephone")
    _city = (By.ID, "input-payment-city")
    _postcode = (By.ID, "input-payment-postcode")
    _password = (By.ID, "input-payment-password")
    _passconfirm = (By.ID, "input-payment-confirm")
    _region_state = (By.ID, "input-payment-zone")
    _region_shipping = (By.ID, "input-shipping-zone")
    _countryPayment = (By.ID, "input-payment-country")
    _countryShipping = (By.ID, "input-shipping-country")
    _privacyPolicyCheckBox = (By.XPATH, "//input[@name='agree']")
    _continueDeliveryDetailsBtn = (By.ID, "button-shipping-address")
    _continueRegisterBtn = (By.ID, "button-register")
    _continueDeliveryMethodBtn = (By.ID, "button-shipping-method")
    _termsCondCheckBox = (By.XPATH, "//input[@name='agree']")
    _continuePaymentBtn = (By.ID, "button-payment-method")
    _confirmOrderBtn = (By.ID, "button-confirm")
    _totalPrice = (By.XPATH, "//*[@id='collapse-checkout-confirm']/div/div[1]/table/tfoot/tr[3]/td[2]")
    _orderTitleConfirmation = (By.TAG_NAME, "h1")
    _continueGuestBtn = (By.ID, "button-guest")
    _radioBtnShippingRate = (By.ID, "//input[@name='shipping_method']")
    _step3Backlink =(By.PARTIAL_LINK_TEXT, "Step 3: Delivery")

    def __init__(self, driver: WebDriver):
        wait: WebDriverWait = WebDriverWait(driver, config.get_explicit_wait_large())
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

    def register_account(self):
        self._click(self._continueBtn)

    def guest_account(self):
        self._click(self._guestRadio)
        self._click(self._continueBtn)

    def fill_all_required_fields_step_registered(self, first_name: str, last_name: str, address1: str, phone: str,
                                      city: str, postcode: str, password: str, passconfirm: str, country: str, state: str):
        email = "qa" + str(randint(0, 100000)) + "@minds.com"
        print("email:", email)
        self._write(self._first_name, first_name)
        self._write(self._last_name, last_name)
        self._write(self._address1, address1)
        self._write(self._emailPayment, email)
        self._write(self._phone, phone)
        self._write(self._city, city)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self._write(self._postcode, postcode)
        self._write(self._password, password)
        self._write(self._passconfirm, passconfirm)
        country_dropdown = Select(self._wait_until_clickable(self._countryPayment))
        country_dropdown.select_by_visible_text(country)
        region_state_dropdown = Select(self._wait_until_clickable(self._region_state))
        region_state_dropdown.select_by_visible_text(state)
        self._click(self._privacyPolicyCheckBox)
        self._click(self._continueRegisterBtn)

    def fill_all_required_fields_step_guest(self, first_name: str, last_name: str, address1: str, phone: str,
                                      city: str, postcode: str, country: str, state: str):
        email = "qa" + str(randint(0, 100000)) + "@minds.com"
        print("email:", email)
        self._write(self._first_name, first_name)
        self._write(self._last_name, last_name)
        self._write(self._address1, address1)
        self._write(self._emailPayment, email)
        self._write(self._phone, phone)
        self._write(self._city, city)
        self._write(self._postcode, postcode)
        self._driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        country_dropdown = Select(self._wait_until_clickable(self._countryPayment))
        country_dropdown.select_by_visible_text(country)
        region_state_dropdown = Select(self._wait_until_clickable(self._region_state))
        region_state_dropdown.select_by_visible_text(state)
        self._click(self._continueGuestBtn)

    def complete_delivery_details_step(self):
        self._click(self._continueDeliveryDetailsBtn)

    def complete_delivery_method_step_for_registered(self):
        time.sleep(4)
        self._click(self._continueDeliveryMethodBtn)
        self._click(self._step3Backlink)
        self._click(self._continueDeliveryDetailsBtn)
        self._click(self._continueDeliveryMethodBtn)

    def complete_delivery_method_step_for_guest(self):
        time.sleep(4)
        self._click(self._continueDeliveryMethodBtn)



    def complete_payment_step(self):
        time.sleep(5)
        self._wait_until_visible(self._termsCondCheckBox)
        self._click(self._termsCondCheckBox)
        self._click(self._continuePaymentBtn)

    def confirm_order_step(self):
        time.sleep(4)
        self._click(self._confirmOrderBtn)
        self._wait_until_visible(self._orderTitleConfirmation)
        time.sleep(4)
        return self._get_element(self._orderTitleConfirmation).text
