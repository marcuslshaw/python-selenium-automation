from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome Browser
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open the URL
driver.get('https://www.target.com')


class SignIn:
    def __init__(self, driver):
        self.driver = driver

    def click_login(self):
        login_button = self.driver.find_element(By.XPATH, "//a[@data-test='@web/AccountLink']")
        login_button.click()
        print("login attempted")
        nav_login_button = self.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']")
        nav_login_button.click()
        print("nav menu login attempted")


def verify_login():
    login = SignIn(driver)
    login.click_login()
    login_page = driver.find_element(By.ID, 'login')
    print("Login page found")


verify_login()

driver.quit()
