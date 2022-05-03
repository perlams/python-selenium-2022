#Ejercicio 6:
#Ir a la página https://demoqa.com/select-menu
#Escribir un script que:
#seleccione de la primera lista Standard Multi Select las opción “Volvo” y “Audi”
#verifique que la opción ha sido seleccionada.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Init Browsers
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select

chrome_driver_path = '../../../drivers/chromedriver'
gecko_driver_path = '../../../drivers/geckodriver'
url = "https://demoqa.com/select-menu"
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)

# Open Web Page
driver.get(url)

# Test Logic
time.sleep(2)
cars = driver.find_element(By.ID, "cars")
assert cars.is_displayed(), "Cars multi select element is not visible"
cars_multiselection = Select(cars)
cars_multiselection.select_by_value("volvo")
cars_multiselection.select_by_value("audi")
selected_option: list = [option.text for option in cars_multiselection.all_selected_options]
assert "Volvo" in selected_option, "Volvo not selected"
assert "Audi" in selected_option, "Audi not selected"
time.sleep(2)


# Cerrar navegador
driver.quit()