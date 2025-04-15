from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Setup
options = Options()
options.add_argument('--headless')  # Run in headless mode
driver = webdriver.Chrome(options=options)

try:
    print("🔍 [Performance Test] Measuring load time for patient registration page...")

    start_time = time.time()

    # Step 1: Load main patient page
    driver.get("https://patient-management-system-phi.vercel.app/")
    
    # Wait for key element (like input field) to ensure page is fully interactive
    driver.find_element("xpath", "//input[@placeholder='John Doe']")  # Example element
    end_time = time.time()

    load_time = round(end_time - start_time, 2)
    print(f"⏱️ Page Load Time: {load_time} seconds")

    # Thresholds can vary. Using 3s here as example
    if load_time <= 3:
        print("✅ Test Passed: Load time within acceptable range.")
    else:
        print("⚠️ Test Warning: Page took longer than 3 seconds to load.")

except Exception as e:
    print(f"❌ Test Failed: Error during performance test — {e}")
finally:
    driver.quit()
