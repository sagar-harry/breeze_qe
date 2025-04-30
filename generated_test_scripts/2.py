
import sys
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popup-blocking")

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Navigate to the homepage
    driver.get("https://www.saucedemo.com/")
    
    # Maximize the window
    driver.maximize_window()

    # Define explicit wait
    wait = WebDriverWait(driver, 10)

    # Wait and perform 'Given I am on the login page'
    time.sleep(3)
    
    # Wait and perform 'When I enter valid username as "validUsername"'
    username_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    username_field.send_keys("validUsername")
    time.sleep(3)

    # Wait and perform 'And I enter an incorrect password as "incorrectPassword"'
    password_field = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
    password_field.send_keys("incorrectPassword")
    time.sleep(3)

    # Wait and perform 'And I click the "Login" button'
    login_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]')))
    login_button.click()
    time.sleep(3)

    # Wait and perform 'Then I should see an error message indicating invalid credentials'
    error_message_present = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@data-test="error"]')))

    # Validate the presence of error message
    if error_message_present:
        print("Test Passed: Error message for invalid credentials is displayed.")
        sys.exit(0)
    else:
        print("Test Failed: No error message found.")
        sys.exit(1)

except NoSuchElementException as e:
    print(f"Test Failed: {str(e)}")
    sys.exit(1)
finally:
    # Clean up
    driver.quit()
