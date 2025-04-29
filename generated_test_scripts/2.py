
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_failed_login_with_incorrect_password():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popups")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the window
        driver.maximize_window()
        
        # Navigate to the home page
        driver.get("https://www.saucedemo.com/")
        
        # Step: Given the user is on the login page
        time.sleep(3)  # Wait for 3 seconds
        
        # Step: When the user enters username "validUser"
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys("validUser")
        time.sleep(3)  # Wait for 3 seconds
        
        # Step: And the user enters incorrect password "wrongPassword"
        password_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_field.send_keys("wrongPassword")
        time.sleep(3)  # Wait for 3 seconds
        
        # Step: And the user clicks the "Login" button
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        time.sleep(3)  # Wait for 3 seconds
        
        # Step: Then the user should see an error message "Invalid username or password"
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//h3[@data-test="error"]'))
        )
        assert "Invalid username or password" in error_message.text
        
        # Exit with success code
        sys.exit(0)
        
    except Exception as e:
        # Print the exception message
        print(f"Test failed: {e}")
        
        # Exit with failure code
        sys.exit(1)
        
    finally:
        # Close the driver
        driver.quit()

# Run the test
test_failed_login_with_incorrect_password()
