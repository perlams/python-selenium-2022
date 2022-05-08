#Ejercicio 9:
#Construir un test que :
#Abra la pagina: https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html
#Presione el botón Download y espere a que se realice la descarga.
#Verificar que la descarga se realizó al 100%

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = '../../../drivers/chromedriver'
gecko_driver_path = '../../../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-download-progress-demo.html'
service = Service(gecko_driver_path)
driver = webdriver.Firefox(service=service)
wait = WebDriverWait(driver, 30)

# Open Web Page
driver.get(url)
driver.maximize_window()

#Click on the download button
btnLocator = (By.ID, "cricle-btn")
btnLocator: WebElement = wait.until(EC.element_to_be_clickable(btnLocator))
btnLocator.click()

# Verify that the file was donloaded at 100%
label = (By.CLASS_NAME, "percenttext")
assert wait.until(EC.text_to_be_present_in_element(label, "100%")), "Label 100% is not present"

# Cerrar navegador
driver.quit()