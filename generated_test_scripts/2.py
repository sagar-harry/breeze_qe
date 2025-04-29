
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_with_incorrect_password():
    # Set up Chrome options to disable notifications, pop-ups, and run in incognito mode
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    chrome_options.add_argument("--incognito")

    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Open the home page
        driver.get("https://www.saucedemo.com/")

        # Maximize the browser window
        driver.maximize_window()

        # Wait for 3 seconds before any action
        wait = WebDriverWait(driver, 10)

        # Locate username field and enter the username
        username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        time.sleep(3)
        username_field.send_keys("validUsername")

        # Locate password field and enter the incorrect password
        password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        time.sleep(3)
        password_field.send_keys("incorrectPassword")

        # Locate and click the login button
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
        time.sleep(3)
        login_button.click()

        # Check for the error message indicating invalid credentials
        error_message = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-test="error"]')))
        time.sleep(3)

        # Validate the presence of the error message
        assert "invalid" in error_message.text.lower(), "Error message not indicating invalid credentials"

        # Exit with code 0 indicating success
        sys.exit(0)
    except Exception as e:
        print(f"Test failed: {e}")

        # Exit with code 1 indicating failure
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_login_with_incorrect_password()
