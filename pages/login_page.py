from selenium import webdriver

from pages.base_page import BasePage
from utils.config_factory import ConfigFactory
from utils.locators import LoginPageLocators


class LoginPage(BasePage):
    def __init__(self, driver: webdriver, config: ConfigFactory):
        """
        Initializes the LoginPage object by calling the __init__ method of the BasePage parent class
        and passing in the webdriver and config objects.
        :param driver: A selenium webdriver object.
        :param config: A ConfigFactory object.
        """
        super().__init__(driver, config)

    def navigate_to_page(self):
        """
        Navigates to the login page URL specified in the config file.
        """
        self.driver.get(self.config.login_url())

    def enter_username(self, username: str):
        """
        Enters the provided username into the username field on the login page.
        :param username: The username to enter.
        """
        self.enter_text(LoginPageLocators.USERNAME, username)

    def enter_password(self, password: str):
        """
        Enters the provided password into the password field on the login page.
        :param password: The password to enter.
        """
        self.enter_text(LoginPageLocators.PASSWORD, password)

    def click_login(self):
        """
        Clicks the login button on the login page.
        """
        self.click_element(LoginPageLocators.LOGIN)

    def get_error_message(self) -> str:
        """
        Retrieves the error message displayed on the login page.
        :return: The error message.
        """
        return self.get_text(LoginPageLocators.LOGIN_ERROR_MESSAGE)
