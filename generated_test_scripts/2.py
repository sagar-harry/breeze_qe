
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--start-maximized")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step: Given the user is on the login page
    driver.get("https://www.saucedemo.com/")

    # Step: When the user enters their username as "validUsername"
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    time.sleep(3)
    username_field.send_keys("validUsername")

    # Step: And the user enters an incorrect password as "incorrectPassword"
    password_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    time.sleep(3)
    password_field.send_keys("incorrectPassword")

    # Step: And the user clicks the "Login" button
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    )
    time.sleep(3)
    login_button.click()

    # Step: Then the user should see an error message saying "Invalid username or password"
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container'))
    )
    time.sleep(3)

    # Validate the error message
    if "Invalid username or password" in error_message.text:
        print("Test Passed: Correct error message displayed")
        sys.exit(0)
    else:
        print("Test Failed: Incorrect error message displayed")
        sys.exit(1)

except Exception as e:
    print(f"Test Failed with exception: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
