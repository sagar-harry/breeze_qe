
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

try:
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--disable-popup-blocking")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    
    # Base URL
    base_url = "https://www.saucedemo.com/"
    
    def perform_login(username, password):
        driver.get(base_url)
        
        # Wait for the username field to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        
        # Input the username
        username_input = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        username_input.clear()
        username_input.send_keys(username)
        
        # Wait for 3 seconds before the next action
        time.sleep(3)

        # Input the password
        password_input = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_input.clear()
        password_input.send_keys(password)
        
        # Wait for 3 seconds before the next action
        time.sleep(3)

        # Click the login button
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        
        # Wait for 3 seconds before the next action
        time.sleep(3)
    
    # Scenario 1: Successful login with valid credentials
    perform_login('standard_user', 'secret_sauce')
    
    # Verifying successful login by checking for the presence of a specific element
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="react-burger-menu-btn"]'))
        )
        print("Test 1: Successful Login - Passed")
    except:
        print("Test 1: Successful Login - Failed")
        sys.exit(1)

    # Scenario 2: Login attempt with invalid credentials
    perform_login('invalid_user', 'invalid_pass')
    
    # Check for the presence of error message
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Epic sadface:')]"))
        )
        print("Test 2: Invalid Credentials - Passed")
    except:
        print("Test 2: Invalid Credentials - Failed")
        sys.exit(1)
    
    # Scenario 3: Attempt to login with empty fields
    perform_login('', '')
    
    # Check for the presence of error message
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//h3[contains(text(), 'Epic sadface:')]"))
        )
        print("Test 3: Empty Fields - Passed")
    except:
        print("Test 3: Empty Fields - Failed")
        sys.exit(1)
    
    # Exit with success status
    sys.exit(0)

except Exception as e:
    print(f'An error occurred: {e}')
    sys.exit(1)

finally:
    # Clean up
    driver.quit()
