from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Start Chrome Browser
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

# Open the URL
driver.get('https://www.target.com')


class CartButton:
    def __init__(self, driver):
        self.driver = driver

    def click_on_cart_button(self):
        cart_button = self.driver.find_element(By.XPATH, "//a[@data-test='@web/CartLink']")
        cart_button.click()
        print("Cart button clicked")

def verify_empty_cart():
    cart = CartButton(driver)
    cart.click_on_cart_button()

    empty_msg = driver.find_element(By.XPATH, "//div[@data-test='boxEmptyMsg']")
    assert "Your cart is empty" in empty_msg.text, "Cart is not empty"
    print("Cart is empty")


# Call the function to verify empty cart
verify_empty_cart()

# Close the browser
driver.quit()

