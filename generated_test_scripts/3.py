
import time
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Maximize the browser window
    driver.maximize_window()

    # Open the home page
    driver.get("https://www.saucedemo.com/")
    
    # Wait for 3 seconds
    time.sleep(3)

    # Wait for the login page to load
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))

    # Enter an incorrect username
    username_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
    username_input.send_keys("incorrect_user")

    # Wait for 3 seconds
    time.sleep(3)

    # Enter the correct password
    password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_input.send_keys("secret_sauce")

    # Wait for 3 seconds
    time.sleep(3)

    # Click the login button
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()
    
    # Wait for 3 seconds
    time.sleep(3)

    # Wait for the error message to appear
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "Username and password do not match any user in this service")]'))
    )

    # Validate that the error message is displayed
    if error_message.is_displayed():
        print("Test case passed: Error message is displayed.")
        driver.quit()
        sys.exit(0)

except Exception as e:
    print(f"Test case failed: {str(e)}")
    driver.quit()
    sys.exit(1)
