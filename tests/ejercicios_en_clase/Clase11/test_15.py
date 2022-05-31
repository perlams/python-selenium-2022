# Ejercicio 15
# Verificar que la opción Currency es Dolar($), luego en la barra de búsqueda, buscar la palabra "Samsung" y seleccionar
# la opción "Samsung SynchMaster 941BW", luego modificar la opción Currency por Euro y verificar que el valor
# del item es menor que el precio en Dolar
import time
from decimal import *

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestCurrency:

    def setup_method(self):
        # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_medium())

        # Abrir la pagina Web
        self.driver.get((config.get_url()))

    def test_display_search(self):
        # Verificar que el simbolo selecionado es $
        currency_loc = (By.CSS_SELECTOR, ".btn-link>strong")
        assert self.wait.until(
            EC.text_to_be_present_in_element(currency_loc, "$")), "The default dollar currency is not set"

        # test_search Input
        searchInput_loc = (By.NAME, "search")
        searchInput: WebElement = self.wait.until(EC.element_to_be_clickable(searchInput_loc))
        searchInput.clear()
        searchInput.send_keys("Samsung")

        # test_search Button
        lookUpBtn_loc = (By.CSS_SELECTOR, ".btn-default")
        lookUpBtn: WebElement = self.wait.until(EC.element_to_be_clickable(lookUpBtn_loc))
        lookUpBtn.click()

        # Select the "SynchMaster 941BW"
        syncMaster_loc = (By.PARTIAL_LINK_TEXT, "SyncMaster 941BW")
        syncMaster: WebElement = self.wait.until(EC.element_to_be_clickable(syncMaster_loc))
        syncMaster.click()

        # Save the dolar price
        price_loc = (By.XPATH, "//*[@id='content']//li/h2")
        price: WebElement = self.wait.until(EC.visibility_of_element_located(price_loc))
        dls_price = float(price.text[1:])

        # Open de Currency dropdown
        currency_loc = (By.XPATH, "//*[@id='form-currency']//button[@data-toggle]")
        currencyDD: WebElement = self.wait.until(EC.element_to_be_clickable(currency_loc))
        currencyDD.click()

        # Select Euro
        euroCurr_loc = (By.NAME, "EUR")
        euroCurr: WebElement = self.wait.until(EC.element_to_be_clickable(euroCurr_loc))
        euroCurr.click()

        # Save the dollar price
        price_loc = (By.XPATH, "//*[@id='content']//li/h2")
        price: WebElement = self.wait.until(EC.visibility_of_element_located(price_loc))
        euro_price = float(price.text[:-1])

        # Verify that the Euro price is cheaper that the Dollar price
        assert dls_price > euro_price, "Euro price is greater that dollar"

    # Close browser
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
