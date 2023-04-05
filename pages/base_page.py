import logging
from typing import Tuple

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.config_factory import ConfigFactory


class BasePage:
    """
    BasePage class serves as the parent class for all the pages in the application.
    It contains methods for interacting with web elements and a shared wait instance.
    """

    def __init__(self, driver: webdriver, config: ConfigFactory):
        """
        Initialize the BasePage class with a webdriver instance and a ConfigFactory instance.
        :param driver: An instance of the webdriver class.
        :param config: An instance of the ConfigFactory class.
        """
        self.driver = driver
        self.config = config
        self._wait = WebDriverWait(self.driver, self.config.timeout())
        self.logger = logging.getLogger(__name__)

    def _find(self, locator: Tuple) -> webdriver.remote:
        """
        Find the element specified by the locator.
        :param locator: Tuple containing the locator of the element.
        :return: The element.
        """
        try:
            return self._wait.until(EC.presence_of_element_located(locator))
        except Exception as e:
            self.logger.exception(
                f"Error while finding element. Locator: {locator}, Error: {e}"
            )
            raise e

    def click_element(self, locator: Tuple):
        """
        Click on an element specified by the locator.
        :param locator: Tuple containing the locator of the element to click on.
        """
        try:
            self._find(locator).click()
        except Exception as e:
            self.logger.exception(
                f"Error while clicking element. Locator: {locator}, Error: {e}"
            )
            raise e

    def enter_text(self, locator: Tuple, text: str):
        """
        Enter text into an element specified by the locator.
        :param locator: Tuple containing the locator of the element to enter text into.
        :param text: The text to enter into the element.
        """
        try:
            element = self._find(locator)
            element.clear()
            element.send_keys(text)
        except Exception as e:
            self.logger.exception(
                f"Error while entering text. Locator: {locator}, Error: {e}"
            )
            raise e

    def get_text(self, locator: Tuple) -> str:
        """
        Get the text of an element specified by the locator.
        :param locator: Tuple containing the locator of the element.
        :return: The text of the element.
        """
        try:
            return self._find(locator).text
        except Exception as e:
            self.logger.exception(
                f"Error while getting text. Locator: {locator}, Error: {e}"
            )
            raise e
