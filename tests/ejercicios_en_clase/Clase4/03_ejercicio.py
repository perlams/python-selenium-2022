#Ejercicio 3:
#Ir a la página https://laboratorio.qaminds.com/
#Escribir un script que:
#Desde la página principal pueda ir a la sección test_login
#Dado un login invalido se muestre un cartel de error con el mensaje:
#“Warning: No match for E-Mail Address and/or Password.”

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

# Localizar el elemento del Menu de MyAccount e interactuar con el
time.sleep(2)
myAccountMenu: WebElement = driver.find_element(By.XPATH, "//a[@title='My Account']")
assert myAccountMenu.is_displayed(), "Menu My Account no disponible"
myAccountMenu.click()

# Localizar el elemento del link de la opcion del Menu e interactuar con el
time.sleep(2)
loginOption: WebElement = driver.find_element(By.LINK_TEXT, "test_login")
assert loginOption.is_displayed(), "Menu test_login no disponible"
loginOption.click()

# Localizar el elemento del textfield del email e interactuar con el
time.sleep(2)
emailTxtField: WebElement = driver.find_element(By.ID, "input-email")
assert emailTxtField.is_displayed(), "El textfield de email no esta disponible"
emailTxtField.send_keys("abcd")

# Localizar el elemento del textfield del password e interactuar con el
time.sleep(2)
passwordTxtField: WebElement = driver.find_element(By.ID, "input-password")
assert passwordTxtField.is_displayed(), "El textfield de email no esta disponible"
passwordTxtField.send_keys("abcd")

# Localizar el elemento del boton de test_login e interactuar con el
time.sleep(2)
loginBtn: WebElement = driver.find_element(By.XPATH, "//input[@type='submit']")
assert loginBtn.is_displayed(), "Boton de test_login no disponible"
loginBtn.click()

# Localizar el elemento del warning de test_login
time.sleep(2)
warning: WebElement = driver.find_element(By.XPATH, "//*[@id='account-login']/div[1]")
assert warning.is_displayed(), "Warning no disponible"
assert warning.text == "Warning: No match for E-Mail Address and/or Password."

# Cerrar navegador
driver.quit()