"""
Product page relate functions
"""

import random

from sauce_lab_automation_assignment.lib.webdriver_utils import WebdriverCommon
from sauce_lab_automation_assignment.pages.product import locators_product


class ProductPage(WebdriverCommon):
    """Product page class"""

    def __init__(self, driver):
        super().__init__(driver)

        self.driver = driver
        self.locator = locators_product

    def wait_for_page_load(self):
        self.wait_for_element(locator_type="class",
                              locator=self.locator.prod_inventory_items)

    def select_random_products(self, num_of_prod):
        """Function selects random product and return its names"""
        product_selected_list = []
        self.wait_for_element(locator_type="class",
                              locator=self.locator.prod_intentory_item)
        products = self.find_elements(locator_type="class",
                                      locator=self.locator.prod_intentory_item)
        random_products = random.choices(products, k=num_of_prod)

        for product in random_products:
            self.wait_for_element(locator_type="class",
                                  locator=self.locator.prod_add_to_cart)
            self.find_element(driver=product, locator_type="class",
                              locator=self.locator.prod_add_to_cart).click()
            product_selected_list.append(
                self.find_element(driver=product, locator_type="class",
                                  locator=self.locator.prod_name).text)

        return product_selected_list
