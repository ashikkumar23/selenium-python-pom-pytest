import pytest
from typing import Tuple

from utils.config_factory import ConfigFactory
from utils.driver_factory import DriverFactory


@pytest.fixture(scope="session")
def driver_config() -> Tuple[DriverFactory, ConfigFactory]:
    """
    Fixture function to set up the driver and configuration objects for test cases.
    :return: Tuple containing the driver object and config object
    """
    driver = DriverFactory().get_driver()
    config = ConfigFactory()
    yield driver, config
    driver.quit()
