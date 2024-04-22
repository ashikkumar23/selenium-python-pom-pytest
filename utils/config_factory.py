from jproperties import Properties


class ConfigFactory:
    """
    A class to handle loading and fetching configuration properties from a file.
    """

    def __init__(self):
        """
        Initialize the ConfigFactory class.
        Loads the properties from the 'resources/config.properties' file.
        """
        self.configs = Properties()
        with open(r"resources/config.properties", "rb") as read_prop:
            self.configs.load(read_prop)

    def fetch(self, property_key: str) -> str:
        """
        Fetch a specific property value by its key.
        :param property_key: The key of the property to fetch.
        :return: The value of the property.
        """
        return self.configs.get(property_key)[0]

    def login_url(self) -> str:
        """
        Fetch the login URL property value.
        :return: The login URL value.
        """
        return self.fetch("LOGIN_URL")

    def browser(self) -> str:
        """
        Fetch the browser property value.
        :return: The browser value.
        """
        return self.fetch("BROWSER")

    def timeout(self) -> int:
        """
        Fetch the timeout property value.
        :return: The timeout value as an integer.
        """
        return int(self.fetch("TIMEOUT"))
