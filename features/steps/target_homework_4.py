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
@given('open target circle')
def open_target(context):
    context.driver.get('https://www.target.com/circle')


@when('verify benefit boxes')
def number_boxes(context):
    num_boxes = context.driver.find_elements(By.CLASS_NAME, "styles__BenefitCard-sc-9mx6dj-2 lgQxFm")

    for num_box in num_boxes:
        text = num_box.txt
        numeric_value = float(text)
        print(numeric_value)

        if numeric_value > 0:
            print(True)

