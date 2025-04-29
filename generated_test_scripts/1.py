
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--incognito")
chrome_options.add_argument("--disable-notifications")
chrome_options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 2})

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

try:
    # Maximize the page
    driver.maximize_window()
    
    # Define wait
    wait = WebDriverWait(driver, 10)
    
    # Navigate to login page
    driver.get("https://www.saucedemo.com/")
    
    # Wait for 3 seconds
    time.sleep(3)
    
    # Given the user is on the login page
    # Locate username field, enter username
    username_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="user-name"]')))
    username_field.send_keys("testUser")
    
    # Wait for 3 seconds
    time.sleep(3)
    
    # Locate password field, enter password
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]')))
    password_field.send_keys("securePassword")
    
    # Wait for 3 seconds
    time.sleep(3)
    
    # Locate and click login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login-button"]')))
    login_button.click()

    # Wait for 3 seconds
    time.sleep(3)
    
    # Then the user should be redirected to the homepage
    # Assuming redirection success is checked by presence of a specific element like a welcome message
    welcome_message = wait.until(EC.presence_of_element_located((By.XPATH, "//h1[contains(text(),'Welcome, testUser!')]")))
    
    # Verify welcome message is displayed (exact locator for welcome message needs to be adjusted according to actual implementation)
    assert "Welcome, testUser!" in welcome_message.text

    # Exit with success code
    sys.exit(0)

except Exception as e:
    print(f"Test failed: {e}")
    # Exit with failure code
    sys.exit(1)

finally:
    # Quit the driver
    driver.quit()
