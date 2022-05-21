from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.login_page import LoginPage


class TestLoginPage:
    driver: WebDriver = None
    login_page: LoginPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        login_page = LoginPage(self.driver)
        login_page.goto("https://laboratorio.qaminds.com/index.php?route=account/login")

    def test_invalid_login(self):
        self.login_page.login("username", "pass")
       # assert self.login_page.is_login_warn_displayed(), "Warn should be displayed"

    def test_forgotten_password(self):
        self.login_page.forgotten_password()

    def test_continue_as_new_customer(self):
        self.login_page.continue_as_new_customer()

    def test_select_menu(self):
        for menu in ['Login', 'Register', 'My Account', 'Address Book', 'Downloads']:
            self.login_page.select_menu(menu)

    def teardown_method(self):
        if self.driver:
            self.driver.quit()
