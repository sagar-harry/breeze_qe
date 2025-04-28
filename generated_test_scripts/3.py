
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def run_test():
    # Setup Chrome options
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
        
        # Input an incorrect username
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username.send_keys("incorrect_username")
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Input a valid password
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password.send_keys("secret_sauce")
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Click the login button
        login_button = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        
        # Wait for 3 seconds
        time.sleep(3)
        
        # Verify the error message indicating invalid credentials
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[contains(text(), "error")]'))
        )
        assert "invalid" in error_message.text.lower()
        
        # If test passed
        sys.exit(0)
    
    except Exception as e:
        print(f"Test failed: {e}")
        sys.exit(1)
    
    finally:
        # Close the WebDriver
        driver.quit()

run_test()
