#Ejercicio 4:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Seleccione la opción Windows que pertenece al menú Laptops & Notebooks
#Verifique que se muestra mensaje indicativo que no existen ítems.
#Verifique que se muestra botón Continue y que si se le hace click, se regresa a la pagina de inicio.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = '../../../drivers/chromedriver'
gecko_driver_path = '../../../drivers/geckodriver'
url = 'https://laboratorio.qaminds.com/'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
driver.maximize_window()

# Abrir pagina
driver.get(url)

# Localizar el elemento Menu Laptops & Notebooks e interactuar con el
time.sleep(2)
laptopsMenu: WebElement = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
assert laptopsMenu.is_displayed(), "Menu Laptops & Notebooks no disponible"
laptopsMenu.click()

# Localizar el elemento Windows de las opciones del dropdown e interactuar con el
time.sleep(2)
windowsOption: WebElement = driver.find_element(By.PARTIAL_LINK_TEXT, "Windows")
assert windowsOption.is_displayed(), "Opcion Windows no disponible"
windowsOption.click()

# Localizar el elemento del mensaje y verificarlo
time.sleep(2)
message: WebElement = driver.find_element(By.XPATH, "//*[@id='content']/p")
assert message.is_displayed(), "Mensaje no disponible"
assert message.text == "There are no products to list in this category."

# Localizar el elemento del boton de Continue e interactuar con el
time.sleep(2)
continueBtn: WebElement = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
assert continueBtn.is_displayed(), "Boton de Continue no disponible"
continueBtn.click()

# Localizar el elemento Logo de la pagina de Home y verificarla
time.sleep(2)
logoImg: WebElement = driver.find_element(By.ID, "logo")
assert logoImg.is_displayed(), "Logo no disponible"


# Cerrar navegador
driver.quit()