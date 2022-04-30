##EJERCICIO 1:
##Ir a la página https://laboratorio.qaminds.com/
##Escribir un script que:
##Permita buscar un iphone desde la barra de búsqueda
##Verificar que devuelve un resultado con una imagen que pertenece a un iphone.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

# Inicializar driver
chrome_driver_path = '../../../drivers/chromedriver'
gecko_driver_path = '../../../drivers/geckodriver'
url = 'https://laboratorio.qaminds.com/'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# Abrir pagina
driver.get(url)

# Localizar el elemento de la barra de busqueda e interactuar con ella
time.sleep(2)
searchInput: WebElement = driver.find_element(By.NAME, "search")
assert searchInput.is_displayed(), "barra no disponible"
searchInput.clear()
searchInput.send_keys("iphone")
searchButton: WebElement = driver.find_element(By.CSS_SELECTOR, ".btn-default")
searchButton.click()
time.sleep(2)
iphoneImage: WebElement = driver.find_element(By.XPATH, "//img[@title='iPhone']")
assert iphoneImage.is_displayed()

# Cerrar navegador
driver.quit()