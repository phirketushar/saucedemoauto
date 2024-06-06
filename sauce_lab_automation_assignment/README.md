
# About Project

Test automation framework for automating product checkout process on www.saucedemo.com.


# Automation Framework Details

It uses Page Object Model Design pattern to automate the UI pages

As per the page, the modules are created, typically contains locator and
the operations supported on the page

Pages are :
* Login Page: It contains functions related to login 
* Product Page: It contains functions to select products
* Checkout Page: It contains functions to verify and proceed on Checkout page

Implementation details:
* Based on python programming language with version 3.8+
* Uses pytest library for running the automated tests
* Uses selenium library to access and automate UI

# Instruction to run
* Install all packages from 'requirement' file
* Automation has support for Chrome browser only. Make sure its installed.
* Go to directory 'sauce_lab_automation_assignment/test'
* Execute command : python -m pytest --html=./log/report.html --self-contained-html
* If encountered with error like 'command not found: python' please use appropriate python executable name
  ex: python3

# Reporting and Log
* HTML reports and logs are generated under directory 'test/log'
