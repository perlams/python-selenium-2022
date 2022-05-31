# Ejercio 11:
# Implementa el patrón Factory para Web Driver que permite poder ejecutar los test cases tanto con Firefox como con Chrome.
# Construye una suite de test case que realice los tests:
# - Búsqueda de Iphone
# - Búsqueda de Tablets
# - Búsqueda de Windows
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from lib.factory.factory_driver import get_driver
from lib.config import config

config.load_config()
print(config.get_implicit_wait())

driver: WebDriver = None


def setup():
    global driver
    config.load_config()
    driver = get_driver()
    driver.maximize_window()
    driver.implicitly_wait(config.get_implicit_wait())


def test_search_Iphone():
    # Abrir pagina
    url = 'https://laboratorio.qaminds.com/'
    driver.get(url)
    searchInput = driver.find_element(By.NAME, "search")
    assert searchInput.is_displayed(), "barra no disponible"
    searchInput.clear()
    searchInput.send_keys("iphone")
    searchButton = driver.find_element(By.CSS_SELECTOR, ".btn-default")
    searchButton.click()
    iphoneImage = driver.find_element(By.XPATH, "//img[@title='iPhone']")
    assert iphoneImage.is_displayed()


def test_search_Tablets():
    url = 'https://laboratorio.qaminds.com/'
    # Abrir pagina
    driver.get(url)
    tabletsMenu = driver.find_element(By.LINK_TEXT, "Tablets")
    assert tabletsMenu.is_displayed(), "menu no disponible"
    tabletsMenu.click()
    samsungItem = driver.find_element(By.LINK_TEXT, "Samsung Galaxy Tab 10.1")
    assert samsungItem.is_displayed(), "item no disponible"
    samsungItem.click()

    price = driver.find_element(By.XPATH, "//*[@id='content']/div/div[2]/ul[2]/li[1]/h2")
    assert price.is_displayed(), "No se encuentra el precio"
    assert price.text == "$241.99", "Precio no es el esperado"

    wishListBtn = driver.find_element(By.XPATH, "//button[@data-original-title='Add to Wish List']")
    wishListBtn.is_displayed(), "No se encuentra el boton de wish list"
    wishListBtn.click()

    addToCartBtn = driver.find_element(By.ID, "button-cart")
    assert addToCartBtn.is_displayed(), "Button not visible"
    addToCartBtn.click()


def test_search_Windows():
    url = 'https://laboratorio.qaminds.com/'
    # Abrir pagina
    driver.get(url)

    # Localizar el elemento Menu Laptops & Notebooks e interactuar con el
    laptopsMenu = driver.find_element(By.LINK_TEXT, "Laptops & Notebooks")
    assert laptopsMenu.is_displayed(), "Menu Laptops & Notebooks no disponible"
    laptopsMenu.click()

    # Localizar el elemento Windows de las opciones del dropdown e interactuar con el
    windowsOption = driver.find_element(By.PARTIAL_LINK_TEXT, "Windows")
    assert windowsOption.is_displayed(), "Opcion Windows no disponible"
    windowsOption.click()

    # Localizar el elemento del mensaje y verificar
    message = driver.find_element(By.XPATH, "//*[@id='content']/p")
    assert message.is_displayed(), "Mensaje no disponible"
    assert message.text == "There are no products to list in this category."

    # Localizar el elemento del boton de Continue e interactuar con el
    continueBtn = driver.find_element(By.CSS_SELECTOR, ".btn-primary")
    assert continueBtn.is_displayed(), "Boton de Continue no disponible"
    continueBtn.click()

    # Localizar el elemento Logo de la pagina de test_home y verificarla
    logoImg = driver.find_element(By.ID, "logo")
    assert logoImg.is_displayed(), "Logo no disponible"


def teardown():
    if driver:
        driver.quit()
