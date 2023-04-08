from pages.base_page import BasePage
from utils.locators import InventoryPageLocators


class InventoryPage(BasePage):
    def get_title(self) -> str:
        """
        This method retrieves the title of the Inventory page.
        :return: The title of the Inventory page.
        """
        return self.get_text(InventoryPageLocators.PRODUCTS)
