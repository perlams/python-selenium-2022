#Ejercicio 10:
#Construir un test que :
#Abra la pagina: https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html
#Presione el la opción Autocloseable success message
#Verificar que se muestra mensaje
#Verificar que mensaje mostrado desaparece después de 5 segundos

from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def click_element(by, value):
    loc = (by,value)
    element: WebElement = wait.until(EC.element_to_be_clickable(loc))
    element.click()

# Setup
chrome_driver_path = '../../../drivers/chromedriver'
gecko_driver_path = '../../../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/bootstrap-alert-messages-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)
driver.maximize_window()

# Click button
click_element(By.ID, "autoclosable-btn-success")

message = (By.CLASS_NAME, "alert-autocloseable-success")
assert wait.until(EC.visibility_of_element_located(message)), "Message was not visible"

# Wait for invisibility
assert wait.until(EC.invisibility_of_element_located(message)), "Message did not disappear"

# Cerrar navegador
driver.quit()