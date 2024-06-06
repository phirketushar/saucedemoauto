"""Steps aggregator file

Consists of all the aggregation functions that interact with different pages
"""


import logging

from sauce_lab_automation_assignment.pages.login.page_login import LoginPage
from sauce_lab_automation_assignment.pages.product.page_product import ProductPage
from sauce_lab_automation_assignment.pages.checkout.page_checkout import CheckoutPage

log = logging.getLogger(__name__)


def perform_login(driver_ob, username, password):
    """Login page function

    It performs the login part
    """
    login_page = LoginPage(driver_ob)
    log.info("Waiting for login page to load")
    login_page.wait_for_page_load()
    log.info("Adding credentials")
    login_page.enter_username(username)
    login_page.enter_password(password)
    login_page.click_login()


def select_random_products(driver_obj, no_of_selection=2):
    """Product page function

    This function select specified number of random products
    """

    product_page = ProductPage(driver_obj)
    log.info("Waiting for product page to load")
    product_page.wait_for_page_load()
    log.info("Selecting random products from list")
    prod_info = product_page.select_random_products(no_of_selection)
    log.info(f"Products selected are: {prod_info}")


def check_out_products(driver_obj, exp_selection, first_name, last_name, zip_code):
    """Checkout page function

    This contains the aggregates steps that perform checout page verification
    and complete the buy process
    """

    checkout_page = CheckoutPage(driver_obj)
    log.info("Navigating to Checkout page")
    checkout_page.navigate_to_checkout_page()
    checkout_page.wait_for_page_load()
    log.info("Verify if the checked out items count")
    checkedout_items = checkout_page.check_number_of_items_added()
    log.info(f"Number of checked out items are {checkedout_items}")
    assert checkedout_items == exp_selection

    # if checkout items are 2 then move forward
    checkout_page.checkout_product()
    log.info("Continuing to add address details and finish")
    checkout_page.checkout_add_first_name(first_name)
    checkout_page.checkout_add_last_name(last_name)
    checkout_page.checkout_add_zip_code(zip_code)
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    log.info("Checking the success message ")
    assert checkout_page.get_success_message(driver_obj) == "Thank you for your order!"
