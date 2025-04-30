
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import sys

def test_login():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-notifications")

    # Initialize the WebDriver
    driver = webdriver.Chrome(options=chrome_options)

    try:
        # Maximize the browser window
        driver.maximize_window()

        # Navigate to the login page
        driver.get("https://www.saucedemo.com/")

        # Wait for 3 seconds
        time.sleep(3)

        # Locate username field and enter username
        username_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_element.send_keys("validUsername")

        # Wait for 3 seconds
        time.sleep(3)

        # Locate password field and enter password
        password_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_element.send_keys("validPassword")

        # Wait for 3 seconds
        time.sleep(3)

        # Locate login button and click
        login_button_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button_element.click()

        # Wait for 3 seconds
        time.sleep(3)

        # Verify redirection to the home page and presence of welcome message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "html"))
        )

        # Check for expected username after login, replace 'WELCOME_MESSAGE_ELEMENT' with actual locator
        try:
            welcome_message_elem = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//span[text()="Welcome, validUsername!"]'))
            )
            # If the welcome message is found, test passes with exit code 0
            if welcome_message_elem.is_displayed():
                sys.exit(0)
        except TimeoutException:
            # If welcome message is not found within the time limit, test fails
            sys.exit(1)

    except Exception as e:
        # If any exception occurs, print it and exit with code 1
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
