"""
Login page relate functions
"""

from sauce_lab_automation_assignment.lib.webdriver_utils import WebdriverCommon
from sauce_lab_automation_assignment.pages.login import locators_login


class LoginPage(WebdriverCommon):
    """Login page class"""

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
        self.locator = locators_login

    def wait_for_page_load(self):
        self.wait_for_element(locator_type="id",
                              locator=self.locator.txt_username)

    def enter_username(self, username):
        self.send_text(locator_type="id",
                       locator=self.locator.txt_username,
                       text=username)

    def enter_password(self, password):
        self.send_text(locator_type="id",
                       locator=self.locator.txt_password,
                       text=password)

    def click_login(self):
        self.click(locator_type="id", locator=self.locator.btn_login)
