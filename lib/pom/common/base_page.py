from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    _driver: WebDriver
    _wait: WebDriverWait

    def __init__(self, driver: WebDriver, wait: WebDriverWait):
        self._driver = driver
        self._wait = wait

    def goto(self, url: str):
        self._driver.get(url)

    def refresh(self):
        self._driver.refresh()

    def close(self):
        self._driver.close()

    def forward(self):
        self._driver.forward()

    def back(self):
        self._driver.back()

    def _click(self, locator: tuple):
        element: WebElement = self._wait_until_clickable(locator)
        element.click()

    def _get_text(self, locator: tuple) -> str:
        element: WebElement = self._wait_until_visible(locator)
        return element.text

    def _get_attribute(self, locator: tuple, attribute: str) -> str:
        element: WebElement = self._wait_until_visible(locator)
        return element.get_attribute(attribute)

    def _write(self, locator: tuple, text: str):
        element: WebElement = self._wait_until_clickable(locator)
        element.clear()
        element.send_keys(text)

    def _write_without_clear(self, locator: tuple, text: str):
        element: WebElement = self._wait_until_clickable(locator)
        element.send_keys(text)

    def _wait_until_clickable(self, locator: tuple) -> WebElement:
        return self._wait.until(EC.element_to_be_clickable(locator))

    def _wait_until_visible(self, locator: tuple) -> WebElement:
        return self._wait.until(EC.visibility_of_element_located(locator))

    def _wait_until_presence(self, locator: tuple) -> WebElement:
        return self._wait.until(EC.presence_of_element_located(locator))

    def _wait_until_visibility_of_all_elements(self, locator: tuple) -> list:
        return self._wait.until(EC.visibility_of_all_elements_located(locator))

    def _get_element(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _get_elements(self, locator: tuple) -> list:
        return self._driver.find_elements(*locator)