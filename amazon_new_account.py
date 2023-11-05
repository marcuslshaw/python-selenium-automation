from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=E2W5VWMST4YG6RCXFM6N&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

# Amazon logo
driver.find_element(By.CSS_SELECTOR, "a[href*='/ref=ap_frn_logo']")
# Create Account
driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")
# Name input box
driver.find_element(By.CSS_SELECTOR, "input#ap_customer_name")
# Email input box
driver.find_element(By.CSS_SELECTOR, "input#ap_email")
# Password input box
driver.find_element(By.CSS_SELECTOR, "input#ap_password")
# Password characters
driver.find_element(By.CSS_SELECTOR, "div.a-alert-content")
# Re-enter password
driver.find_element(By.CSS_SELECTOR, "input#ap_password_check")
# Continue button
driver.find_element(By.CSS_SELECTOR, "input#continue")
# Conditions of Use
driver.find_element(By.CSS_SELECTOR, "[href*='condition_of_use']")
# Privacy Notice
driver.find_element(By.CSS_SELECTOR, "[href*='privacy_notice']")
# Sign in
driver.find_element(By.CSS_SELECTOR, "[href*='signin?openid'")

# verify results
print('Test Passed')
