
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import sys

def test_login_with_incorrect_password():
    # Initialize WebDriver options
    options = webdriver.ChromeOptions()
    options.add_argument('--incognito')
    options.add_argument('--disable-notifications')
    
    # Initialize the WebDriver
    driver = webdriver.Chrome(options=options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the home page
        driver.get("https://www.saucedemo.com/")

        # Wait for the login elements to load
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]')))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="login-button"]')))

        # Background: Given the user is on the login page
        time.sleep(3)

        # Scenario: Fail to login with incorrect password
        # When the user enters their username
        username_field = driver.find_element(By.XPATH, '//*[@id="user-name"]')
        username_field.send_keys("standard_user")

        # And the user enters an incorrect password
        password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
        password_field.send_keys("incorrect_password")

        # And the user clicks the 'Login' button
        login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
        login_button.click()

        time.sleep(3)

        # Then the user should see an error message indicating an incorrect password
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@data-test="error"]')))
        
        if error_message.is_displayed():
            print("Error message is correctly displayed: Test Passed")
            sys.exit(0)
        else:
            print("Error message is not displayed: Test Failed")
            sys.exit(1)

    except Exception as e:
        print("An exception occurred: ", str(e))
        sys.exit(1)
    finally:
        # Close the browser
        driver.quit()

test_login_with_incorrect_password()
