
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configuration
options = webdriver.ChromeOptions()
options.add_argument("--incognito")
options.add_argument("--disable-notifications")
options.add_argument("--start-maximized")

# Setting up the WebDriver
driver = webdriver.Chrome(options=options)

try:
    # Step 1: Go to the home page
    driver.get("https://www.saucedemo.com/")

    # Step 2: Wait for 3 seconds
    time.sleep(3)

    # Background: The User is on the Login Page
    # Already handled by navigating to the URL

    # Scenario: Fail to login with incorrect username

    # Step 3: The User enters an incorrect username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    username_field.send_keys("incorrect_username")

    # Step 4: Wait for 3 seconds
    time.sleep(3)

    # Step 5: The User enters a valid password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password_field.send_keys("secret_sauce")

    # Step 6: Wait for 3 seconds
    time.sleep(3)

    # Step 7: The User clicks the 'Login' button
    login_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
    )
    login_button.click()

    # Step 8: Wait for 3 seconds
    time.sleep(3)

    # Step 9: The User should see an error message indicating login failure
    error_message_present = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//h3[@data-test="error"]'))
    )

    if error_message_present:
        print("Test Case Passed: Error message is displayed.")
        sys.exit(0)
    else:
        print("Test Case Failed: Error message not displayed.")
        sys.exit(1)

except Exception as e:
    print(f"Exception occurred: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
