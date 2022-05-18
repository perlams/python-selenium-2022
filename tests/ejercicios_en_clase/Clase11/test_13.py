# Ejercicio 13
# Buscar la palabra "Display", validar que se muestra un mensaje de que no existen productos con la busqueda.
# Seleccionar la opción "Search in product descriptions" y volver a realizar la busqueda anterio, validar que ahora se muestran 4 resultados.

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestSearch:

    def setup_method(self):
        #Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_medium())

        #Abrir la pagina Web
        self.driver.get((config.get_url()))

    def test_display_search(self):
        # Search Input
        searchInput_loc = (By.NAME, "search")
        searchInput: WebElement = self.wait.until(EC.element_to_be_clickable(searchInput_loc))
        searchInput.clear()
        searchInput.send_keys("Display")

        #Search Button
        lookUpBtn_loc = (By.CSS_SELECTOR, ".btn-default")
        lookUpBtn: WebElement = self.wait.until(EC.element_to_be_clickable(lookUpBtn_loc))
        lookUpBtn.click()

        #No products msg
        message = (By.XPATH, "//*[@id='content']/p[2]")
        no_prod_msg = "There is no product that matches the search criteria."
        assert self.wait.until(EC.text_to_be_present_in_element(message,
                                                                no_prod_msg)), "The text is not the expected one"

        # Checkbox
        checkbox_loc = (By.ID, "description")
        checkboxDescription: WebElement = self.wait.until(EC.element_to_be_clickable(checkbox_loc))
        checkboxDescription.click()
        assert checkboxDescription.is_selected()

        #Search Button
        searchBtn_loc = (By.ID, "button-search")
        searchBtn: WebElement = self.wait.until(EC.element_to_be_clickable(searchBtn_loc))
        searchBtn.click()

        # Find all products
        products_loc = (By.XPATH, "//*[@class='caption']//a")
        products: list = self.wait.until(EC.visibility_of_all_elements_located(products_loc))
        for product in products:
            print(product.text)
            assert product.text in ['Apple Cinema 30"', 'iPod Nano', 'iPod Touch', 'MacBook Pro']

    # Close browser
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
