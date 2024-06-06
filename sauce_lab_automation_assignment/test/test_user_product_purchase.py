"""

Test file to do user product buying scenarios
"""
import logging
import pytest

from sauce_lab_automation_assignment.steps import user_process_aggregator

from sauce_lab_automation_assignment.configs import data_file

log = logging.getLogger(__name__)


@pytest.mark.parametrize('test_data', data_file.product_purchase)
def test_buy_product(browser_obj, test_data):
    """Test to perform user product buy"""

    uname = test_data["username"]
    pwd = test_data["password"]
    product_selection = test_data["product_to_select"]
    checkout_addr_first_name = test_data["checkout_addr_first_name"]
    checkout_addr_last_name = test_data["checkout_addr_last_name"]
    checkout_addr_zip_code = test_data["checkout_addr_zip_code"]

    log.info("Starting with SuaceDemo product checkout test")
    log.info(f"Username specified is {uname} and password is {pwd}")
    # login to the web page
    user_process_aggregator.perform_login(browser_obj, uname, pwd)
    log.info("Login is successful, proceeding to random product selection")

    # Select products
    user_process_aggregator.select_random_products(browser_obj, product_selection)
    log.info("Product selection is complete, moving to checkout")

    # Checkout the products
    user_process_aggregator.check_out_products(browser_obj,
                                               product_selection,
                                               checkout_addr_first_name,
                                               checkout_addr_last_name,
                                               checkout_addr_zip_code)
    log.info("Completed with the execution of test case")
