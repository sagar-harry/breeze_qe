
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import time

def test_login_scenarios():
    try:
        # Set up Chrome options
        options = webdriver.ChromeOptions()
        options.add_argument("--incognito")
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-popup-blocking")
        driver = webdriver.Chrome(options=options)

        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the home page
        driver.get("https://www.saucedemo.com/")
        
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )

        # Scenario 1: Successful login with valid credentials
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("valid_username")  # Replace with valid credentials
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("valid_password")  # Replace with valid password
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        WebDriverWait(driver, 10).until(
            EC.title_contains("Products")
        )

        # Perform check for a welcome message on the dashboard
        # Assuming that a welcome message or specific element is present on the page. This should be modified to match actual application
        welcome_displayed = driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
        assert welcome_displayed is True, "Welcome message not displayed after login"
        
        # Log out to proceed to the next test
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(3)
        driver.find_element(By.ID, "logout_sidebar_link").click()

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login-button"))
        )

        # Scenario 2: Unsuccessful login with invalid credentials
        time.sleep(3)
        driver.find_element(By.ID, "user-name").send_keys("invalid_username")
        time.sleep(3)
        driver.find_element(By.ID, "password").send_keys("invalid_password")
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()
        time.sleep(3)

        error_displayed = driver.find_element(By.XPATH, "//*[contains(text(), 'Username and password do not match')]").is_displayed()
        assert error_displayed is True, "Error message not displayed for invalid credentials"

        # Scenario 3: Validate login error without credentials
        time.sleep(3)
        driver.find_element(By.NAME, "user-name").clear()
        driver.find_element(By.NAME, "password").clear()
        time.sleep(3)
        driver.find_element(By.ID, "login-button").click()

        missing_cred_error_displayed = driver.find_element(By.XPATH, "//*[contains(text(), 'Username is required')]").is_displayed()
        assert missing_cred_error_displayed is True, "Error message not displayed for missing credentials"

        # Exit with code 0 if all tests passed
        sys.exit(0)

    except Exception as e:
        print("Test failed:", e)
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login_scenarios()
