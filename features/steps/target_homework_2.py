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


@when('Click sign in')
def click_sign_in(context):
    # context.driver.implicitly_wait(10)
    context.driver.find_element(By.CSS_SELECTOR, "span.styles__LinkText-sc-1e1g60c-3").click()
    # context.driver.find_element(By.XPATH, "//a[@href='/account?prehydrateClick=true']").click()
    # sleep(7)


@when('Navigation Menu')
def nav_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()


@then('Sign In')
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "button#login").click()
    print("Test Passed")
