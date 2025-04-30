
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    
    # Maximize the browser window
    driver.maximize_window()

    # Navigate to the login page
    driver.get("https://www.saucedemo.com/")
    
    # Wait for 3 seconds
    time.sleep(3)
    
    # Define locators
    username_locator = (By.XPATH, '//*[@id="user-name"]')
    password_locator = (By.XPATH, '//*[@id="password"]')
    login_button_locator = (By.XPATH, '//*[@id="login-button"]')
    error_message_locator = (By.XPATH, '//*[contains(text(), "Epic sadface:")]')

    # Wait for the username field and enter the incorrect username
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(username_locator))
    driver.find_element(*username_locator).send_keys("incorrect_username")

    # Wait for 3 seconds
    time.sleep(3)

    # Wait for the password field and enter the valid password
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(password_locator))
    driver.find_element(*password_locator).send_keys("secret_sauce")

    # Wait for 3 seconds
    time.sleep(3)

    # Wait for the login button and click it
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(login_button_locator))
    driver.find_element(*login_button_locator).click()

    # Wait for 3 seconds
    time.sleep(3)

    # Verify the presence of the error message
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(error_message_locator))
    
    # Exit with code 0 if test case passed
    sys.exit(0)

except Exception as e:
    print("Test case failed:", e)
    # Exit with code 1 if test case failed
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
