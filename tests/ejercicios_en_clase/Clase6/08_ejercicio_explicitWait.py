#Ejercicio 8:
#Construir un test que :
#Abra la pagina: https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html
#Presione el botón Start Download y espere a que se realice la descarga.
#Verificar que aparece el mensaje: Complete
#Verificar que aparece el botón Close

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = '../../../drivers/chromedriver'
gecko_driver_path = '../../../drivers/geckodriver'
url = 'https://demo.seleniumeasy.com/jquery-download-progress-bar-demo.html'
service = Service(chrome_driver_path)
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)

# Open Web Page
driver.get(url)
driver.maximize_window()

#Click download
download_loc = (By.ID, "downloadButton")
download: WebElement = wait.until(EC.element_to_be_clickable(download_loc))
download.click()


# Verify progress label
progress_label_loc = (By.CSS_SELECTOR, ".progress-label")
assert wait.until(EC.text_to_be_present_in_element(progress_label_loc, "Complete!")), "Complete! not in the progress label"


# Verify continue button
close_btn_local = (By.XPATH, "//button[text()='Close']")
close_btn: WebElement = wait.until(EC.element_to_be_clickable(close_btn_local))
close_btn.click()

# Cerrar navegador
driver.quit()

