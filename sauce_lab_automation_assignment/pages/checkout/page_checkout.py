"""
Checkout page related functions
"""

from sauce_lab_automation_assignment.lib.webdriver_utils import WebdriverCommon
from sauce_lab_automation_assignment.pages.checkout import locators_checkout


class CheckoutPage(WebdriverCommon):
    """Checkout page class"""

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
        self.locator = locators_checkout

    def navigate_to_checkout_page(self):
        self.click(locator_type="class", locator=self.locator.checkout_link)

    def wait_for_page_load(self):
        self.wait_for_element(locator_type="class",
                              locator=self.locator.checkout_cart_list)

    def check_number_of_items_added(self):
        self.wait_for_element(locator_type="class",
                              locator=self.locator.checkout_cart_item)
        products = self.find_elements(locator_type="class",
                                      locator=self.locator.checkout_cart_item)
        return len(products)

    def checkout_product(self):
        self.click(locator_type="id", locator=self.locator.btn_checkout)

    def checkout_add_first_name(self, fist_name):
        self.wait_for_element(locator_type="id",
                              locator=self.locator.txt_first_name)
        self.send_text(locator_type="id",
                       locator=self.locator.txt_first_name,
                       text=fist_name)

    def checkout_add_last_name(self, last_name):
        self.send_text(locator_type="id",
                       locator=self.locator.txt_last_name,
                       text=last_name)

    def checkout_add_zip_code(self, zip_code):
        self.send_text(locator_type="id",
                       locator=self.locator.txt_postal_code,
                       text=zip_code)

    def continue_checkout(self):
        self.click(locator_type="id", locator=self.locator.btn_continue)

    def finish_checkout(self):
        self.click(locator_type="id", locator=self.locator.btn_finish)

    def get_success_message(self, driver):
        return self.find_element(driver=driver,
                                 locator_type="class",
                                 locator=self.locator.txt_success).text
