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


driver.find_element(By.CSS_SELECTOR, '.a-link-nav-icon')

driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

driver.find_element(By.CSS_SELECTOR, '#ap_email')

driver.find_element(By.CSS_SELECTOR, '#ap_password')

driver.find_element(By.CSS_SELECTOR, '.a-box-inner.a-alert-container')

driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

driver.find_element(By.CSS_SELECTOR, '#continue')

driver.find_element(By.CSS_SELECTOR, "[href*='condition']")

driver.find_element(By.CSS_SELECTOR, "[href*='notification_privacy']")

driver.find_element(By.CSS_SELECTOR, '.a-link-emphasis')