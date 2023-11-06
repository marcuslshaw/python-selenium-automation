from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from behave import given, when, then
from time import sleep


@when('search for {item}')
def item_search(context, item):
    search_input = context.driver.find_element(By.ID, "search")
    search_input.clear()
    search_input.send_keys(item)
    search_input.send_keys(Keys.ENTER)
    sleep(4)


@when('add {item} to cart')
def add_to_cart(context, item):
    context.driver.find_element(By.XPATH, "//div[contains(@class, 'ProductCardImageWrapper-sc-164r5os-0')]").click()
    sleep(4)
    add_to_cart_button = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor86216293")
    add_to_cart_button.click()
    sleep(4)
    context.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()
    sleep(4)


@then('verify {item} in cart')
def item_in_cart(context, item):
    cart_item = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cart-summary-title']")
    print(cart_item.text)
