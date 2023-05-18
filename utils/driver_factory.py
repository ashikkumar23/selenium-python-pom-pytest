from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from utils.config_factory import ConfigFactory


class DriverFactory:
    """
    A class to manage the drivers.
    """

    @staticmethod
    def set_chrome_options() -> webdriver.ChromeOptions():
        """
        Returns an instance of ChromeOptions class which can be used to set options for the Chrome driver.
        :return: An instance of ChromeOptions
        """
        return webdriver.ChromeOptions()

    @staticmethod
    def set_firefox_options() -> webdriver.FirefoxOptions():
        """
        Returns an instance of FirefoxOptions class which can be used to set options for the Firefox driver.
        :return: An instance of FirefoxOptions
        """
        return webdriver.FirefoxOptions()

    def get_driver(self) -> webdriver:
        """
        Returns an instance of webdriver based on the browser configured in the config_factory.
        :return: An instance of webdriver
        :raises Exception: If the browser choice is invalid
        """
        browser = ConfigFactory().browser()
        if browser == "chrome":
            driver = webdriver.Chrome(
                options=self.set_chrome_options(),
                service=ChromeService(ChromeDriverManager().install()),
            )
            return self._browser_settings(driver)
        elif browser == "firefox":
            driver = webdriver.Firefox(
                options=self.set_firefox_options(),
                service=FirefoxService(GeckoDriverManager().install()),
            )
            return self._browser_settings(driver)
        else:
            raise Exception(f"Invalid browser choice: {browser}!")

    @staticmethod
    def _browser_settings(driver):
        driver.implicitly_wait(ConfigFactory().timeout())
        driver.maximize_window()
        return driver
