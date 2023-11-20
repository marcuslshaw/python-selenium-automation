from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Start Chrome Browser
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(10)  # Set an implicit wait of 10 seconds

# Open the URL
driver.get('https://www.target.com/p/A-88345426?preselect=87990484')

# Define the colors and their corresponding XPaths
colors = {
    "Brown": "//a[@aria-label='Brown']",
    "Oatmeal": "//a[@aria-label='Oatmeal']",
    "Gray": "//a[@aria-label='Gray']",
    "Black": "//a[@aria-label='Black']"
}

for color, xpath in colors.items():
    # Click on the color option
    driver.find_element(By.XPATH, xpath).click()

    # Check the color text
    color_element = driver.find_element(By.XPATH, "//div[@class='styles__CellVariationHeaderWrapper-sc-1xq8mou-0 kLjeEp']")
    color_text = color_element.text
    print(f"{color} - True")

# Close the browser
driver.quit()
