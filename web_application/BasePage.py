import logging
import polling
from typing import Optional, List

from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from config.config import Config as cf


class BasePage:
    def __init__(self, driver):
        self.logger = logging.getLogger("ui_auto_tests" + f".{self.__class__.__name__}")
        self.driver: WebDriver = driver
        self.timeout = cf.web_ui_wait_timeout
        self.wait = WebDriverWait(self.driver, self.timeout, ignored_exceptions=[StaleElementReferenceException])

    def find_element(self, locator, clickable=False) -> Optional[WebElement]:
        element = None
        try:
            element = self.wait.until(ec.presence_of_element_located(locator))
            if clickable:
                element = self.wait.until(ec.element_to_be_clickable(locator))
        except TimeoutException:
            self.logger.info(f"BasePage:find_element:Timed out waiting for page to load for {locator}")
        except StaleElementReferenceException:
            self.logger.info(f"BasePage:find_element:Element {locator} is not attached to the page document")
        return element

    def is_element_present(self, locator, timeout: int = cf.web_ui_wait_timeout) -> bool:
        try:
            wait = WebDriverWait(self.driver, timeout=timeout, ignored_exceptions=[StaleElementReferenceException])
            wait.until(ec.visibility_of_element_located(locator)).is_displayed()
            return True
        except TimeoutException:
            return False

    def wait_for_page_load(self, locator):
        try:
            self.wait.until(ec.presence_of_element_located(locator))
        except TimeoutException as e:
            self.logger.error("BasePage:wait_for_page_load:Timed out waiting for page to load")
            raise e

    def find_elements(self, locator: str) -> Optional[List[WebElement]]:
        try:
            return self.wait.until(ec.presence_of_all_elements_located(locator))
        except TimeoutException:
            self.logger.info(f"Elements not found: {locator}")
        except StaleElementReferenceException:
            self.logger.info(f"BasePage:find_element:Element {locator} is not attached to the page document")

    def wait_text_element_loaded(self, locator):
        polling.poll(
            target=lambda: self.find_element(locator).text != "",
            step=1,
            timeout=3,
        )
