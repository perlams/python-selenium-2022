from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.login_page import LoginPage


class TestLoginPage:
    driver: WebDriver = None
    login_page: LoginPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        login_page = LoginPage(self.driver)
        login_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=samsung")


    def test_get_product_information(self):
        pass

    def test_add_to_cart(self):
        pass

    def test_get_total_reviews(self):
        pass

    def teardown_method(self):
        if self.driver:
            self.driver.quit()