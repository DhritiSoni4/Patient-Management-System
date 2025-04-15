from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
options = Options()
options.add_argument('--headless')  # Optional: run browser in headless mode
driver = webdriver.Chrome(options=options)

try:
    print("🔍 [Test] Unauthorized Admin Access Check")
    
    # Step 1: Navigate directly to admin page (bypassing passkey modal)
    driver.get("https://patient-management-system-phi.vercel.app/?admin=true")
    time.sleep(2)

    # Step 2: Check if passkey modal still shows
    modal_present = False
    try:
        modal = driver.find_element(By.XPATH, "//h2[contains(text(),'Admin Access Verification')]")
        if modal.is_displayed():
            modal_present = True
    except:
        modal_present = False

    # Assert: Passkey modal should be present
    if modal_present:
        print("✅ Test Passed: Unauthorized access is blocked. Passkey modal is shown.")
    else:
        print("❌ Test Failed: Admin dashboard accessible without passkey!")

except Exception as e:
    print(f"⚠️ Exception occurred: {e}")
finally:
    driver.quit()
