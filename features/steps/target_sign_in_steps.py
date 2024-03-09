from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In')
def click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='LinkText']").click()


@when('From right side navigation menu, click Sign In')
def from_right_side_click_sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.driver.find_element(By.CSS_SELECTOR, "[method='post']")
    print('Test case passed')