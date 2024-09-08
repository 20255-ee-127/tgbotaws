from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
time.sleep(12)
# Function to start scraping
def start_scraping(driver):
    try:
        # Wait for the element with the class name "title QljEeKI5" to be present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ChatInfo .title.QljEeKI5 .fullName'))
        )
        
        # Print the text of the element
        print(element.text)

        # Wait for a short period of time to reduce the number of requests
        time.sleep(0.001)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to send a message
def send_message(driver, message):
    try:
        # Wait for the message input field to be present
        message_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#editable-message-text'))
        )
        
        # Type the message
        message_input.send_keys(message)
        
        # Wait for a short period of time to ensure the message is typed
        time.sleep(1)
        
        # Wait for the send button to be clickable
        send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, 'button.Button.send.main-button.default.secondary.round.click-allowed'))
        )
        
        # Click the send button
        send_button.click()
        
        print("Message sent successfully.")
    except Exception as e:
        print(f"An error occurred while sending the message: {e}")

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
    print("opened telegram")
    # Wait for user to log in manually
    # input("Please log in to Telegram and then press Enter here...")
    driver.get("https://web.telegram.org/a/manu")
    print("opened manu")
    # Navigate to the specific chat URL
    driver.get("https://web.telegram.org/a/#-1002343236358")
    print("got chat")
    # Wait for the page to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.ChatInfo'))
    )
    
    # Start scraping
    start_scraping(driver)
    
    # Send a message
    message = "hi selling bitdefender at 49rs for 3 months on your gmail with warranty"
    send_message(driver, message)
    print("Send msg")
    time.sleep(2)
    
finally:
    # Close the WebDriver
    driver.quit()