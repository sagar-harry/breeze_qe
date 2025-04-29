
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_failed_login_incorrect_username():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")
    
    # Initialize WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Navigate to the webpage
        driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        time.sleep(3)

        # Wait for the username field and enter incorrect username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys("incorrect_username")
        time.sleep(3)

        # Wait for the password field and enter valid password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_field.send_keys("secret_sauce")  # Assuming this is a valid password
        time.sleep(3)

        # Wait for the login button and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        time.sleep(3)

        # Wait for the error message indicating an incorrect username
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'error-message-container')]"))
        )
        assert "Epic sadface: Username and password do not match any user in this service" in error_message.text

        # If it reaches here without exception, the test is successful
        print("Test Passed")
        sys.exit(0)

    except Exception as e:
        # Print the exception message for any test failure
        print(f"Test Failed: {e}")
        sys.exit(1)

    finally:
        # Clean up and close the browser
        driver.quit()

# Run the test
test_failed_login_incorrect_username()
