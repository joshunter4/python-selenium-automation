from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()
driver.implicitly_wait(5)

driver.get('https://www.target.com/')

driver.find_element(By.XPATH, "//*[@data-test='@web/AccountLink']").click()

driver.find_element(By.XPATH, "//*[@data-test='accountNav-signIn']").click()

expected = 'Sign into your Target account'

driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']")

driver.find_element(By.ID, 'login')
