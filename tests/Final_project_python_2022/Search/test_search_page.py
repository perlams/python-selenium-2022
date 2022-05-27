from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestSearch:

    def setup_method(self):
        # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_medium())

        # Abrir la pagina Web
        self.driver.get((config.get_url()))

    def test_search_for_a_valid_product(self):
        # Search Input
        searchInput_loc = (By.NAME, "search")
        searchInput: WebElement = self.wait.until(EC.element_to_be_clickable(searchInput_loc))
        searchInput.clear()
        searchInput.send_keys("Samsung")

        # Search Button
        lookUpBtn_loc = (By.CSS_SELECTOR, ".btn-default")
        lookUpBtn: WebElement = self.wait.until(EC.element_to_be_clickable(lookUpBtn_loc))
        lookUpBtn.click()

        # Select the "SynchMaster 941BW"
        syncMaster_loc = (By.PARTIAL_LINK_TEXT, "SyncMaster 941BW")
        syncMaster: WebElement = self.wait.until(EC.element_to_be_clickable(syncMaster_loc))
        syncMaster.click()

    def test_search_for_non_existing_product(self):
        # Search Input
        searchInput_loc = (By.NAME, "search")
        searchInput: WebElement = self.wait.until(EC.element_to_be_clickable(searchInput_loc))
        searchInput.clear()
        searchInput.send_keys("Display")

        # Search Button
        lookUpBtn_loc = (By.CSS_SELECTOR, ".btn-default")
        lookUpBtn: WebElement = self.wait.until(EC.element_to_be_clickable(lookUpBtn_loc))
        lookUpBtn.click()

        # No products msg
        message = (By.XPATH, "//*[@id='content']/p[2]")
        no_prod_msg = "There is no product that matches the search criteria."
        assert self.wait.until(EC.text_to_be_present_in_element(message,
                                                                    no_prod_msg)), "The text is not the expected one"

    # Close browser
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
