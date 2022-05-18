# Ejercicio 14
# Ir a la selección Desktops y seleccionar la opción Mac, verificar que se muestra un item con el titulo iMac. Abrir el producto
# y agregarlo al carrito, luego verificar que aparece en el botón del carrito la información "1 ite(s) - $122.00"

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from lib.factory.factory_driver import get_driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lib.config import config


class TestAddToCart:

    def setup_method(self):
        # Crear nueva instancia de WebDriver utilizando factory driver
        self.driver: WebDriver = get_driver()

        # Crear instancia de WebDriverWait
        self.wait: WebDriverWait = WebDriverWait(self.driver, config.get_explicit_wait_medium())

        # Abrir la pagina Web
        self.driver.get((config.get_url()))

    def test_add_to_cart(self):

        # Abrir el menu de desktops
        menu_desktop = (By.LINK_TEXT, "Desktops")
        desktop: WebElement = self.wait.until(EC.element_to_be_clickable(menu_desktop))
        desktop.click()

        #Abrir el menu de Mac
        menu_mac = (By.PARTIAL_LINK_TEXT, "Mac")
        desktop: WebElement = self.wait.until(EC.element_to_be_clickable(menu_mac))
        desktop.click()

        # Abrir el link de iMac
        iMac_loc = (By.LINK_TEXT, "iMac")
        iMac: WebElement = self.wait.until(EC.element_to_be_clickable(iMac_loc))
        iMac.click()

        # Agregar el item al carrito
        addToCart_loc = (By.ID, "button-cart")
        addToCartBtn: WebElement = self.wait.until(EC.element_to_be_clickable(addToCart_loc))
        addToCartBtn.click()

        # Verificar la Alerta
        alert_loc = (By.CLASS_NAME, "alert-success")
        assert self.wait.until(
            EC.text_to_be_present_in_element(alert_loc,
                                             "Success: You have added iMac to your shopping cart!")), "The expected result is not present"
        # Verificar que aparece en el botón del carrito la información
        blackLblCart_loc = (By.ID, "cart-total")
        assert self.wait.until(
            EC.text_to_be_present_in_element(blackLblCart_loc,
                                             "1 item(s) - $122.00")), "The expected result is not present"

    # Close browser
    def teardown_method(self):
        if self.driver:
            self.driver.quit()
