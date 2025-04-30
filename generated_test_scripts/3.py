
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_with_invalid_username():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize browser window
        driver.maximize_window()

        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")

        # Wait for 3 seconds
        time.sleep(3)

        # Locate username field and enter an incorrect username
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys("incorrect_user")
        
        # Wait for 3 seconds
        time.sleep(3)

        # Locate password field and enter a valid password
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_field.send_keys("secret_sauce")
        
        # Wait for 3 seconds
        time.sleep(3)

        # Locate and click on the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        
        # Wait for 3 seconds
        time.sleep(3)

        # Verify the error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(
                (By.XPATH, '//*[@data-test="error"]')
            )
        )
        
        if "invalid" in error_message.text.lower():
            print("Test Passed: Invalid login error message is displayed.")
            sys.exit(0)
        else:
            print("Test Failed: Expected error message not displayed.")
            sys.exit(1)

    except Exception as e:
        print(f"Test Failed: {str(e)}")
        sys.exit(1)
    
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_login_with_invalid_username()
