from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.pom.qaminds.product_page import ProductPage


class TestProductPage:
    driver: WebDriver = None
    prod_page: ProductPage = None

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        prod_page = ProductPage(self.driver)
        prod_page.goto("https://laboratorio.qaminds.com/index.php?route=product/product&product_id=33&search=samsung")

    def test_get_product_information(self):
        name = self.prod_page.get_name()
        assert name == "Samsung SyncMaster 941BW"

        price = self.prod_page.get_price()
        assert price == "189.87€"

        ex_tax = self.prod_page.get_ex_tax()
        assert ex_tax == "Ex Tax: 156.92€"

        prod_code = self.prod_page.get_product_code()
        assert prod_code == "Product Code: Product 6"

        prod_availability = self.prod_page.get_availability()
        assert prod_availability == "Availability: In Stock"

        prod_desc = self.prod_page.get_description()
        assert prod_desc == "True"

    def test_add_to_cart(self):
        self.prod_page.add_to_cart()
        self.prod_page.is_login_warn_displayed()

    def test_get_total_reviews(self):
        reviews = self.prod_page.get_total_reviews()
        assert reviews == "0"

    def teardown_method(self):
        if self.driver:
            self.driver.quit()
