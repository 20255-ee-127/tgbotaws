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

# Function to send a message
def send_message(driver, message):
    try:
        # Find the message input field
        message_input = driver.find_element(By.CSS_SELECTOR, '#editable-message-text')
        
        # Type the message
        message_input.send_keys(message)
        
        # Wait for a short period of time to ensure the message is typed
        time.sleep(1)
        
        # Find the send button
        send_button = driver.find_element(By.CSS_SELECTOR, 'button.Button.send.main-button.default.secondary.round.click-allowed')
        
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
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

driver = webdriver.Chrome(options=chrome_options)

try:
    # Open Telegram Web
    driver.get("https://web.telegram.org/a/")
    
    # Wait for user to log in manually
    # input("Please log in to Telegram and then press Enter here...")
    driver.get("https://web.telegram.org/a/manu")
    # Navigate to the specific chat URL
    driver.get("https://web.telegram.org/a/#-1001426208123")
    
    # Wait for the page to load
    # input("Press Enter after the page has loaded...")
    # Wait for 2 seconds
    time.sleep(2)
    # Start scraping
    start_scraping(driver)
    
    # Send a message
    message = "hi selling bitdefender at 49rs for 3 months on your gmail with warranty"
    time.sleep(2)
    send_message(driver, message)
    input('closing')
finally:
    # Close the WebDriver
    driver.quit()