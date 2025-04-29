
import time
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")  # Incognito mode
chrome_options.add_argument("--disable-notifications")  # Disable notifications
chrome_options.add_argument("--disable-popup-blocking")  # Disable popup blocking

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Open the home page
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()  # Maximize the window
    time.sleep(3)  # Wait for 3 seconds

    # Wait for the username field to be present and enter incorrect username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]'))
    )
    username_field.send_keys("incorrect_username")
    time.sleep(3)  # Wait for 3 seconds

    # Enter a valid password
    password_field = driver.find_element(By.XPATH, '//*[@id="password"]')
    password_field.send_keys("secret_sauce")
    time.sleep(3)  # Wait for 3 seconds

    # Click the 'Login' button
    login_button = driver.find_element(By.XPATH, '//*[@id="login-button"]')
    login_button.click()
    time.sleep(3)  # Wait for 3 seconds

    # Verify the error message
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@data-test="error"]')
        )
    )

    # Check if the error message is displayed with relevant text
    if error_message.is_displayed() and "Username and password do not match any user in this service" in error_message.text:
        print("Test Passed: Error message displayed as expected.")
        sys.exit(0)
    else:
        print("Test Failed: Error message not displayed or incorrect.")
        sys.exit(1)

except Exception as e:
    print(f"Test Failed: {e}")
    sys.exit(1)
finally:
    # Close the browser
    driver.quit()
