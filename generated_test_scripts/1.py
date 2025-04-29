
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--disable-notifications")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Maximize the window
    driver.maximize_window()
    
    # Navigate to the homepage
    driver.get("https://www.saucedemo.com/")
    
    # Scenario 1: Enter username and password on the login page
    try:
        # Wait for page to load
        time.sleep(3)
        
        # Enter username
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        time.sleep(3)
        
        # Enter password
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        time.sleep(3)
        
        # Click login button
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)
        
        # Verify redirection to the dashboard
        WebDriverWait(driver, 10).until(EC.url_contains("https://www.saucedemo.com/inventory.html"))
        
        # Verify presence of a welcome message or dashboard element
        # Example check: presence of "fleece jacket" element
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))

        print("Test case Scenario 1 passed")
    except Exception as e:
        print(f"Test case Scenario 1 failed: {e}")
        sys.exit(1)

    # Scenario 2: Enter username and password on the login page with validation on another page
    try:
        # Log out to return to login page
        # Click side bar
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-burger-menu-btn"]'))).click()
        time.sleep(3)
        # Log out
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="logout_sidebar_link"]'))).click()
        time.sleep(3)

        # Repeat login process
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))).send_keys("standard_user")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))).send_keys("secret_sauce")
        time.sleep(3)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))).click()
        time.sleep(3)
        
        # Verify redirection to the dashboard
        WebDriverWait(driver, 10).until(EC.url_contains("https://www.saucedemo.com/inventory.html"))
        
        # Verify presence of a welcome message or dashboard element
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')))

        print("Test case Scenario 2 passed")
    except Exception as e:
        print(f"Test case Scenario 2 failed: {e}")
        sys.exit(1)

    # If all scenarios pass
    sys.exit(0)

finally:
    # Quit the driver
    driver.quit()
