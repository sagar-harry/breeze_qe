
import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def setup_driver():
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    return driver

def wait_for_element(driver, by, value):
    try:
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((by, value)))
        return element
    except:
        print(f"Element with {by} = {value} not found.")
        driver.quit()
        sys.exit(1)

def test_login_functionality():
    # Initialize WebDriver
    driver = setup_driver()
    driver.get("https://www.saucedemo.com/")
    
    try:
        # Login
        time.sleep(3)
        username = wait_for_element(driver, By.XPATH, '//*[@id="user-name"]')
        username.send_keys("Username")
        time.sleep(3)
        
        password = wait_for_element(driver, By.XPATH, '//*[@id="password"]')
        password.send_keys("Password")
        time.sleep(3)
        
        login_button = wait_for_element(driver, By.XPATH, '//*[@id="login-button"]')
        login_button.click()
        time.sleep(3)
        
        # Verify redirection to the dashboard
        dashboard_url = "https://www.saucedemo.com/inventory.html"  # Assuming this is the dashboard URL
        assert driver.current_url == dashboard_url, "Failed to redirect to dashboard."
        
        # Check for welcome message (placeholders since no locator provided)
        welcome_message = wait_for_element(driver, By.XPATH, '//h2[contains(text(), "Welcome")]')
        assert "Welcome" in welcome_message.text, "Welcome message not displayed on dashboard."
        
        # Validation across pages
        driver.get(dashboard_url)
        time.sleep(3)
        
        assert "Welcome" in welcome_message.text, "Welcome message not persistent on dashboard."
        
        # Validation after login on a different page
        profile_url = "https://www.saucedemo.com/profile.html"  # Assuming this is the profile page URL
        driver.get(profile_url)
        time.sleep(3)
        
        # Profile information check (placeholders since no locator information provided)
        profile_info = wait_for_element(driver, By.XPATH, '//div[@class="profile-info"]')
        assert "User Info" in profile_info.text, "User information not displayed on profile page."
    
        # If all assertions pass
        print("All tests passed.")
        driver.quit()
        sys.exit(0)

    except AssertionError as e:
        print(f"Assertion Error: {e}")
        driver.quit()
        sys.exit(1)

if __name__ == "__main__":
    test_login_functionality()
