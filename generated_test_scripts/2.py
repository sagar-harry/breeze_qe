
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_with_incorrect_password():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")
    
    # Initialize the Chrome driver
    driver = webdriver.Chrome(options=chrome_options)
    try:
        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")
        
        # Wait for the username field and enter the valid username
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        time.sleep(3)
        username_field.send_keys("validUsername")
        
        # Wait for the password field and enter the invalid password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        time.sleep(3)
        password_field.send_keys("invalidPassword")
        
        # Wait for the login button and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        time.sleep(3)
        login_button.click()
        
        # Wait for the error message to appear
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, 'error-message-container'))
        )
        time.sleep(3)
        
        # Verify if error message is displayed
        if error_message.is_displayed():
            print("Test case passed: Error message displayed as expected.")
            sys.exit(0)
        else:
            print("Test case failed: Error message not displayed.")
            sys.exit(1)
    except Exception as e:
        print(f"Test case failed: {e}")
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

# Execute the test function
if __name__ == "__main__":
    test_login_with_incorrect_password()
