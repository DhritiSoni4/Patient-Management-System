from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up browser
driver = webdriver.Chrome()
driver.get("https://patient-management-system-phi.vercel.app/")
driver.maximize_window()

try:
    # Fill form
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@placeholder="John Doe"]')))
    driver.find_element(By.XPATH, '//input[@placeholder="John Doe"]').send_keys("Test User")
    driver.find_element(By.XPATH, '//input[@placeholder="johndoe@gmail.com"]').send_keys("testuser123@example.com")
    driver.find_element(By.XPATH, '//input[@type="tel"]').send_keys("1234567890")
    print("[✓] Patient info filled.")

    # Click "Get Started"
    driver.find_element(By.XPATH, '//button[contains(text(), "Get Started")]').click()
    print("[✓] Clicked Get Started.")

    # Wait for page change
    time.sleep(3)

    # Check if redirected to known pages
    current_url = driver.current_url
    if "/register" in current_url or "/appointments" in current_url:
        print("✅ Test Case Passed")
    else:
        print("❌ Test Case Failed")

except Exception as e:
    print("❌ Test Failed with error:", str(e))

finally:
    time.sleep(2)
    driver.quit()
