
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Initialize the driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Open the home page
    driver.get("https://www.saucedemo.com/")
    time.sleep(3)  # Wait for 3 seconds before the next action

    # Step 2: Enter the username
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    username_input.send_keys("exampleUser")
    time.sleep(3)  # Wait for 3 seconds before the next action

    # Step 3: Enter the password
    password_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password_input.send_keys("examplePassword123")
    time.sleep(3)  # Wait for 3 seconds before the next action

    # Step 4: Click the 'Login' button
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
    )
    login_button.click()
    time.sleep(3)  # Wait for 3 seconds before the next action

    # Step 5: Verify redirection to the dashboard
    # Assuming the dashboard page contains a specific element as its identifying feature
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(text(),'Welcome, exampleUser')]"))
    )

    print("Test case passed")
    sys.exit(0)

except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

finally:
    driver.quit()
