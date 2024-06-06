"""Default file of pytest

It contains all the common functions and fixtures
"""

import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def browser_obj(url="https://www.saucedemo.com"):
    """Webdriver object

    This object will be used throughout the automation to execute
    different selenium commands
    """
    driver = webdriver.Chrome()
    driver.get(url=url)
    driver.maximize_window()
    yield driver
    driver.close()
