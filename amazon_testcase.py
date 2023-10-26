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
driver.get('https://www.amazon.com')

# search by xpath
driver.find_element(By.ID, "nav-orders").click()

# wait for 4 sec
sleep(4)

# search by xpath
driver.find_element(By.XPATH, "//h1[@class='a-spacing-small']")
driver.find_element(By.XPATH, "//input[@id='ap_email']")

# verify results
print('Test Passed')

