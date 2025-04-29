
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Test Data
home_page_url = "https://www.saucedemo.com/"
incorrect_username = "wrong_user"
valid_password = "secret_sauce"

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disable-popups")

# Initialize WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Step 1: Navigate to the Login page
    driver.maximize_window()
    driver.get(home_page_url)

    # Step 2: Wait and Enter an incorrect username
    time.sleep(3)
    username_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    username_element.clear()
    username_element.send_keys(incorrect_username)

    # Step 3: Wait and Enter a valid password
    time.sleep(3)
    password_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
    )
    password_element.clear()
    password_element.send_keys(valid_password)

    # Step 4: Wait and Click the Login button
    time.sleep(3)
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
    )
    login_button.click()

    # Step 5: Wait and Assert error message is displayed
    time.sleep(3)
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h3[contains(@data-test, 'error')]"))
    )
    
    # Ensure user remains on the Login page
    assert driver.current_url == home_page_url, "Failed: Did not remain on the Login page."

    print("Test Passed: Error message is displayed and user remains on the Login page.")
    sys.exit(0)

except Exception as e:
    print(f"Test Failed: {e}")
    sys.exit(1)

finally:
    # Close the browser
    driver.quit()
