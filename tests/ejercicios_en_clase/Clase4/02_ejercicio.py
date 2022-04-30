##EJERCICIO 2:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Seleccione la opción Tablets
#Deberá aparecer un item con titulo: Samsung Galaxy Tab 10.1
#Seleccionar dicho item
#Verifique que:El costo del item es de $241.99
#Puede agregarlo a una Whist List
#Puede agregarlo al Carrito

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
tabletsMenu: WebElement = driver.find_element(By.LINK_TEXT, "Tablets")
assert tabletsMenu.is_displayed(), "menu no disponible"
tabletsMenu.click()
time.sleep(2)
samsungItem: WebElement = driver.find_element(By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
assert samsungItem.is_displayed(), "item no disponible"
samsungItem.click()
time.sleep(2)

price: WebElement = driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/ul[2]/li[1]/h2")
assert price.is_displayed(), "No se encuentra el precio"
assert price.text == "$241.99", "Precio no es el esperado"

wishListBtn: WebElement = driver.find_element(By.XPATH,"//button[@data-original-title='Add to Wish List']")
wishListBtn.is_displayed(), "No se encuentra el boton de wish list"
wishListBtn.click()

addToCartBtn: WebElement = driver.find_element(By.ID, "button-cart")
assert addToCartBtn.is_displayed(), "Button not visible"
addToCartBtn.click()

# Cerrar navegador
driver.quit()