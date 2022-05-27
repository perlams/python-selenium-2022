from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config
from lib.pom.qaminds.home_page import HomePage


class TestHomePage:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.driver.get(config.get_url())

    def test_home_logo(self):
        # 1. Find the logo's image
        home_page = HomePage(self.driver)
        assert home_page.is_logo_visible(), 'Logo should be visible'

    def test_home_menus(self):
        #  1. Click on tablets menu
        #  2. Click on software menu
        home_page = HomePage(self.driver)
        home_page.select_menu("Tablets")
        home_page.select_menu("Software")

    def test_home_submenus(self):
        #  1. Click on menu components -> monitors
        #  2. Select Apple Cinema 30"
        home_page = HomePage(self.driver)
        home_page.select_sub_menu("Components", "Monitors")
        home_page.select_product('Apple Cinema 30"')

    def test_home_currency(self):
        #  1. Verify currency, most be same symbol as $
        #  2. Change to Eur currency
        home_page = HomePage(self.driver)
        assert "$" == home_page.get_currency()
        home_page.set_currency("EUR")
        assert "€" == home_page.get_currency()

    def test_home_cart(self):
        # 1. Verify text in the shopping cart, with the expected value: 0 item(s) - $0.00
        home_page = HomePage(self.driver)
        total = home_page.get_cart_total()
        assert "0 item(s) - $0.00" == total

    def teardown_method(self):
        if self.driver:
            self.driver.quit()