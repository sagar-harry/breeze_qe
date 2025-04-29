
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException

def test_login():
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--start-maximized")

    # Initialize the web driver
    driver = webdriver.Chrome(options=chrome_options)

    # Gherkin: Given I am on the login page
    driver.get("https://www.saucedemo.com/")

    try:
        # Maximize the window
        driver.maximize_window()

        # Add sleep before each action
        time.sleep(3)

        # Gherkin: When I enter a valid username
        username_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        username_element.send_keys("standard_user")

        time.sleep(3)

        # Gherkin: And I enter a valid password
        password_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_element.send_keys("secret_sauce")

        time.sleep(3)

        # Gherkin: And I click the "Login" button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()

        time.sleep(3)

        # Gherkin: Then I should be redirected to the homepage
        WebDriverWait(driver, 10).until(
            EC.url_to_be("https://www.saucedemo.com/inventory.html")
        )

        # Gherkin: And I should see a welcome message (we assume welcome message exists as part of the homepage verification)
        # Checking for the inventory page's typical element as a placeholder for 'Welcome message'
        inventory_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, '//*[@id="inventory_container"]'))
        )

        time.sleep(3)

        # Test Passed
        sys.exit(0)

    except TimeoutException as e:
        print(f"Test failed: {e}")
        sys.exit(1)

    finally:
        driver.quit()

if __name__ == "__main__":
    test_login()
