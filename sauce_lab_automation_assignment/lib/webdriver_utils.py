"""
Webdriver common operations
"""

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

TIMEOUT = 20


class WebdriverCommon:
    """Common webelement class"""

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator_type, locator):
        """Simulate Click operation"""
        # by = self.get_locator_type(locator_type)
        self.wait_for_element(locator_type, locator)
        self.find_element(self.driver, locator_type, locator).click()

    def find_element(self, driver, locator_type, locator):
        """Simulate Find Element operation"""
        # if not locator_type:
        locator_type = self.get_locator_type(locator_type)
        return driver.find_element(by=locator_type, value=locator)

    def find_elements(self, locator_type, locator):
        """Simulate Find Elements operation"""
        # if not locator_type:
        locator_type = self.get_locator_type(locator_type)
        return self.driver.find_elements(by=locator_type, value=locator)

    def wait_for_element(self, locator_type, locator):
        """Simulate WaitforElement operation"""
        # if not locator_type:
        locator_type = self.get_locator_type(locator_type)
        WebDriverWait(self.driver, TIMEOUT).until(
            EC.presence_of_element_located((locator_type, locator)))

    def send_text(self, locator_type, locator, text):
        """Simulate send_text operation"""
        self.wait_for_element(locator_type, locator)
        self.find_element(self.driver, locator_type, locator).send_keys(text)

    def get_locator_type(self, loc_type):
        """returns the locator type as per text provided"""
        map_dict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "class": By.CLASS_NAME
        }
        return map_dict[loc_type]
