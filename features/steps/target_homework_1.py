from selenium import webdriver
from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#  Start Chrome Browser
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)


# Open target.com
@given('Open Target page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Cart was clicked on')
def click_cart_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "image[href*='Cart.svg#Cart']").click()


@then('Cart is empty')
def verify_empty(context):
    context.driver.find_element(By.CSS_SELECTOR, "div[data-test='boxEmptyMsg'] h1")
    print("Test Passed")

