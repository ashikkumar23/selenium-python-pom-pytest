from typing import Tuple

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    """
    A class that holds the locators for the login page elements.
    """

    USERNAME: Tuple = (By.ID, "user-name")
    PASSWORD: Tuple = (By.ID, "password")
    LOGIN: Tuple = (By.ID, "login-button")
    LOGIN_ERROR_MESSAGE: Tuple = (By.CLASS_NAME, "error-message-container")


class InventoryPageLocators(object):
    """
    A class that holds the locators for the Inventory page elements.
    """

    PRODUCTS: Tuple = (By.XPATH, "//span[contains(text(),'Products')]")
    LOGOUT: Tuple = (By.XPATH, "//a[@id='logout_sidebar_link']")
