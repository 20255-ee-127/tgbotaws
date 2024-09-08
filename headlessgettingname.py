from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

# Function to start scraping
def start_scraping(driver):
    try:
        # Find the element with the class name "title QljEeKI5"
        element = driver.find_element(By.CSS_SELECTOR, '.ChatInfo .title.QljEeKI5 .fullName')
        
        # Print the text of the element
        print(element.text)

        # Wait for a short period of time to reduce the number of requests
        time.sleep(0.001)
    except Exception as e:
        print(f"An error occurred: {e}")

# Path to the Chrome profile directory
profile_dir = os.path.expanduser("~/.chrome/profile")

# Create a new instance of the Chrome driver with the specified profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=" + profile_dir)
chrome_options.add_argument("--start-maximized")  # Start maximized
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (recommended for headless mode)
chrome_options.add_argument("--window-size=1920,1080")  # Set window size (recommended for headless mode)

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Telegram Web
    driver.get("https://web.telegram.org/a/")
    
    # Wait for user to log in manually
    input("Please log in to Telegram and then press Enter here...")
    driver.get("https://web.telegram.org/a/manu")
    input("go")
    # Navigate to the specific chat URL
    driver.get("https://web.telegram.org/a/#-1001764208660")
    
    # Wait for the page to load
    input("Press Enter after the page has loaded...")

    # Start scraping
    start_scraping(driver)

finally:
    # Close the WebDriver
    driver.quit()