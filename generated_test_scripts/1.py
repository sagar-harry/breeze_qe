
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def main():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    try:
        # Given the user is on the login page
        driver.get("https://www.saucedemo.com/")
        time.sleep(3)

        # When the user enters the username "testuser"
        user_name_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
        )
        user_name_input.send_keys("testuser")
        time.sleep(3)

        # And the user enters the password "securepassword"
        password_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="password"]'))
        )
        password_input.send_keys("securepassword")
        time.sleep(3)

        # And the user clicks the 'Login' button
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]'))
        )
        login_button.click()
        time.sleep(3)

        # Then the user should be redirected to the validation page
        # Assuming validation page has a specific element as an identifier (replace with actual identifier)
        validation_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[text()="Welcome, testuser!"]'))
        )

        # And the user should see a message "Welcome, testuser!" on the validation page
        assert "Welcome, testuser!" in validation_message.text
        sys.exit(0)

    except Exception as e:
        print(f"Test Failed: {e}")
        sys.exit(1)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
