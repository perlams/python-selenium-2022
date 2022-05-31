from random import randint

from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage
from lib.pom.qaminds.checkout_page import CheckoutPage


class TestCheckoutPage:
    driver: WebDriver = None
    prod_page: ProductPage = None
    checkout_page: CheckoutPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.prod_page = ProductPage(self.driver)
        self.prod_page.goto(
            "https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=samsung")
        self.prod_page.add_to_cart()
        self.prod_page.is_login_warn_displayed()
        self.checkout_page = CheckoutPage(self.driver)
        self.checkout_page.goto(
            "https://laboratorio.qaminds.com/index.php?route=checkout/checkout")

    def test_checkout_invalid_customer(self):
        invalid_email = "qa" + str(randint(0, 100000)) + "@minds.com"
        print("email:", invalid_email)
        password = "3422134"
        expected_error_msg = "Warning: No match for E-Mail Address and/or Password."
        assert expected_error_msg == self.checkout_page.login_with_invalid_credentials(invalid_email, password)[:53]

    def test_checkout_valid_customer(self):
        valid_email = "qa@minds.com"
        password = "12345"
        expected_title_msg = "Checkout"
        assert expected_title_msg == self.checkout_page.login_with_valid_credentials(valid_email, password)

    def test_checkout_forgotten_password(self):
        expected_title_msg = "Forgot Your Password?"
        assert expected_title_msg == self.checkout_page.forgotten_password()

    def test_checkout_complete_an_order_as_a_registered_user(self):
        first_name = "QA"
        last_name = "Minds"
        address1 = "P.sherman calle wallaby 42"
        phone = "6666666666"
        city = "Zapopan"
        postcode = "44879"
        password = "12345"
        country = "Mexico"
        state = "Tabasco"
        confirmation_message = "Your order has been placed!"
        self.checkout_page.register_account()
        self.checkout_page.fill_all_required_fields_step_registered(first_name, last_name, address1, phone, city, postcode,
                                                         password, password, country, state)
        self.checkout_page.complete_delivery_method_step_for_registered()
        self.checkout_page.complete_payment_step()
        assert confirmation_message == self.checkout_page.confirm_order_step()

    def test_checkout_complete_an_order_as_a_guest_user(self):
        first_name = "QA"
        last_name = "Minds"
        address1 = "P.sherman calle wallaby 42"
        phone = "6666666666"
        city = "Zapopan"
        postcode = "44879"
        country = "Mexico"
        state = "Tabasco"
        confirmation_message = "Your order has been placed!"
        self.checkout_page.guest_account()
        self.checkout_page.fill_all_required_fields_step_guest(first_name, last_name, address1, phone, city, postcode, country,  state)
        self.checkout_page.complete_delivery_method_step_for_guest()
        self.checkout_page.complete_payment_step()
        assert confirmation_message == self.checkout_page.confirm_order_step()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()
