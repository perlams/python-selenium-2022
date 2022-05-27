from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.register_page import RegisterPage


class TestRegisterPage:
    driver: WebDriver = None
    register_page: RegisterPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.register_page = RegisterPage(self.driver)
        self.register_page.goto(
            "https://laboratorio.qaminds.com/index.php?route=account/register")

    def test_register_user_with_valid_info(self):
        first_name = "QA"
        last_name = "Minds"
        phone = "3333333333"
        password = "12345"
        confirm_password = "12345"
        expected_successful_msg = "Your Account Has Been Created!"
        assert expected_successful_msg == self.register_page.complete_form_valid_values(first_name, last_name, phone, password,
                                                      confirm_password)

    def test_register_submit_incomplete_form(self):
        self.register_page.submit_an_incomplete_form()
        expected_err_msg_first_name = "First Name must be between 1 and 32 characters!"
        expected_err_msg_last_name = "Last Name must be between 1 and 32 characters!"
        expected_err_msg_email_name = "E-Mail Address does not appear to be valid!"
        expected_err_msg_phone_name = "Telephone must be between 3 and 32 characters!"
        expected_err_msg_password_name = "Password must be between 4 and 20 characters!"
        assert expected_err_msg_first_name == self.register_page.get_first_name_error()
        assert expected_err_msg_last_name == self.register_page.get_last_name_error()
        assert expected_err_msg_email_name == self.register_page.get_email_error()
        assert expected_err_msg_phone_name == self.register_page.get_phone_error()
        assert expected_err_msg_password_name == self.register_page.get_password_error()

    def teardown_method(self):
        if self.driver:
            self.driver.quit()
