# Ejercicio 11:
# Utilizando Page Factory poder llamar al browser especifico con llamar a la funcion de get_drver

import time
from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver

class TestPageFactory:

    def setup_method(self):
        # Call the Page Factory

        #driver = get_driver()
        self.driver: WebDriver = get_driver()

        # Open Web Page
        url = 'https://qamindslab.com'
        self.driver.get(url)
        time.sleep(3)

        # Close browser
        self.driver.quit()