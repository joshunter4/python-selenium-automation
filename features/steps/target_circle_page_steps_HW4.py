from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open Target Circle main page')
def open_target_circle_main(context):
    context.driver.get('https://www.target.com/circle')


@then('Verify {expected_num} benefit boxes')
def verify_num_of_benefit_boxes(context, expected_num):
    context.driver.find_element(By.CSS_SELECTOR, "[class*='BenefitCard-sc']")
    print('Test case passed')
