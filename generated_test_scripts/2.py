
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_with_incorrect_password():
    # Options for Chrome driver
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    
    # Instantiate the Chrome WebDriver
    driver = webdriver.Chrome(options=options)
    
    try:
        # Navigate to the home page
        driver.get("https://www.saucedemo.com/")
        
        # Maximize the browser window
        driver.maximize_window()

        # Wait for 3 seconds before performing any actions
        time.sleep(3)
        
        # Locate the username field and enter a valid username
        username_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_field.send_keys("valid.username@example.com")
        
        # Wait for 3 seconds before performing any actions
        time.sleep(3)
        
        # Locate the password field and enter an incorrect password
        password_field = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_field.send_keys("incorrectPassword123")
        
        # Wait for 3 seconds before performing any actions
        time.sleep(3)
        
        # Locate the login button and click it
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        
        # Wait for 3 seconds before performing any actions
        time.sleep(3)
        
        # Assert that the error message is displayed
        error_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "//h3[@data-test='error']"))
        )
        
        if error_message.text == "Invalid username or password":
            print("Test case passed.")
            sys.exit(0)
        else:
            print("Test case failed.")
            sys.exit(1)
            
    except Exception as e:
        print("Exception occurred:", e)
        print("Test case failed.")
        sys.exit(1) 
    finally:
        # Close the browser
        driver.quit()

if __name__ == "__main__":
    test_login_with_incorrect_password()
