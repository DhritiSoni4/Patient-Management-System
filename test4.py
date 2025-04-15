from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://patient-management-system-phi.vercel.app/?admin=true")
driver.maximize_window()

try:
    time.sleep(2)

    print("[🔐] Entering passkey: 111111")

    # Locate the single hidden input field
    passkey_input = driver.find_element(By.XPATH, "//input[@inputmode='numeric']")

    passkey_input.send_keys("111111")

    time.sleep(1)

    # Click the 'Enter Admin Passkey' button
    submit_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Enter Admin Passkey')]")
    submit_btn.click()

    time.sleep(2)

    # Verify redirection or dashboard element
    if "/admin" in driver.current_url or "Dashboard" in driver.page_source:
        print("✅ Test Passed: Admin access granted.")
    else:
        print("❌ Test Failed: Invalid passkey or redirection failed.")

except Exception as e:
    print(f"⚠️ Error: {e}")

finally:
    driver.quit()
