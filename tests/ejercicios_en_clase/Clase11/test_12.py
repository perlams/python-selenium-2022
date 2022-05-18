from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestDownload:

    def setup_method(self):
        self.driver: WebDriver = get_driver()
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_large())

    def test_download_button_1(self):
        """Ejercicio 8"""
        # Open web page
        self.driver.get("https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html")

        # Click download
        download_loc = (By.ID, "downloadButton")
        download: WebElement = self.wait.until(EC.element_to_be_clickable(download_loc))
        download.click()

        # Verify progress label
        progress_label_loc = (By.CLASS_NAME, "progress-label")  # XPATH: //*[@class='progress-label']
        self.wait.until(EC.text_to_be_present_in_element(progress_label_loc, "Complete!"))

        # Verify continue button
        close_btn_local = (By.XPATH, "//button[text()='Close']")
        close_btn: WebElement = self.wait.until(EC.element_to_be_clickable(close_btn_local))
        close_btn.click()

    def test_download_button_2(self):
        """Ejercicio 9"""
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html")
        btnLocator = (By.ID, "cricle-btn")
        btnLocator: WebElement = self.wait.until(EC.element_to_be_clickable(btnLocator))
        btnLocator.click()

        # Verify that the file was donloaded at 100%
        label = (By.CLASS_NAME, "percenttext")
        assert self.wait.until(EC.text_to_be_present_in_element(label, "100%")), "Label 100% is not present"

    def click_element(by, value, self):
        loc = (by, value)
        element: WebElement = self.wait.until(EC.element_to_be_clickable(loc))
        element.click()

    def test_auto_closable_msg(self):
        """Ejercicio 10"""
        self.driver.get("https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html")
        element_loc = (By.ID, "autoclosable-btn-success")
        element : WebElement = self.wait.until(EC.element_to_be_clickable(element_loc))
        element.click()
        self.click_element
        message = (By.CLASS_NAME, "alert-autocloseable-success")
        assert self.wait.until(EC.visibility_of_element_located(message)), "Message was not visible"
        # Wait for invisibility
        assert self.wait.until(EC.invisibility_of_element_located(message)), "Message did not disappear"

    def teardown_method(self):
        if self.driver:
            self.driver.quit()