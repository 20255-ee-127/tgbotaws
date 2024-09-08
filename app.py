from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import os
import random

# Dictionary to store peer IDs and group names
group_dict = {
    "-1001590039268": "INDIAN OTP GROUP SELLER BUYER GROUPS",
    "-1001488908424": "NETFLIX BUYING AND SELLING 2.O",
    "-1001649688493":"Indian Buy and Sell",
    "-1001621438661":"Magnus Billing India",
    "-1001659476892":"PUBLIC ESCROW SERVICE",
    "-1002228599896":"BUYING AND SELLING GROUP TELEGRAM",
    "-1001185878771":"SELLING CITY",
    "-1001380837716":"Selling_premium",
    "-1001701127261":"Swiggy no 1 mod apk",
    "-1001760505674":"Trusted Mod Discussion®™"
    # Add more peer IDs and group names as needed
}

# Function to start scraping
def start_scraping(driver):
    try:
        # Wait for the element with the class name "title QljEeKI5" to be present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.ChatInfo .title.QljEeKI5 .fullName'))
        )
        
        # Print the text of the element
        print("Chat Name:", element.text)

        # Wait for a short period of time to reduce the number of requests
        time.sleep(0.001)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to get the message content
def get_message_content(driver):
    try:
        # Wait for the element with the class name "content-inner" to be present
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.content-inner .text-content'))
        )
        
        # Print the text of the element
        print("Message Content:", element.text)

        # Wait for a short period of time to reduce the number of requests
        time.sleep(0.001)
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to forward the message
def forward_message(driver, peer_id):
    try:
        # Wait for the message element to be present
        message_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.content-inner .text-content'))
        )
        
        # Hover over the message element to make the forward button visible
        actions = ActionChains(driver)
        actions.move_to_element(message_element).perform()
        
        # Wait for the forward button to be present and click it
        forward_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '.message-action-buttons .Button[aria-label="Forward"]'))
        )
        forward_button.click()
        
        # Wait for the forward input field to be present
        forward_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.Transition_slide-active .form-control[placeholder="Forward to..."]'))
        )
        
        # Enter the group name from the dictionary
        forward_input.send_keys(group_dict[peer_id])
        
        # Wait for the group option to be present and click it
        group_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//div[contains(@class, "picker-list custom-scroll")]//div[@data-peer-id="{peer_id}"]'))
        )
        group_option.click()
        
        # Wait for the final send button to be present and click it
        final_send_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#MiddleColumn .Button.send.main-button.default.secondary.round.click-allowed[aria-label="Send Message"]'))
        )
        final_send_button.click()
        
        print(f"Message forwarded successfully to {group_dict[peer_id]}.")
    except Exception as e:
        print(f"An error occurred while forwarding the message to {group_dict[peer_id]}: {e}")

# Path to the Chrome profile directory
profile_dir = os.path.expanduser("~/.chrome/profile")

# Create a new instance of the Chrome driver with the specified profile directory
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--user-data-dir=" + profile_dir)
chrome_options.add_argument("--start-maximized")  # Start maximized
# chrome_options.add_argument("--headless")  # Uncomment this line to run in headless mode

driver = webdriver.Chrome(options=chrome_options)

for peer_id in group_dict.keys():
    try:
        # Open Telegram Web
        driver.get("https://web.telegram.org/a/")
        input("Please log in to Telegram and then press Enter here...")
        driver.get("https://web.telegram.org/a/manu")
        # Navigate to the specific chat URL
        driver.get("https://web.telegram.org/a/#-1002443402979")
        
        # Wait for the page to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.content-inner'))
        )
        time.sleep(random.randint(3, 6))
        # Start scraping
        start_scraping(driver)
        time.sleep(random.randint(3, 6))
        # Get the message content
        get_message_content(driver)
        time.sleep(random.randint(3, 6))
        
        # Forward the message
        forward_message(driver, peer_id)
        # Generate a random sleep time between 10 and 20 seconds
        sleep_time = random.randint(30, 60)
        time.sleep(sleep_time)
    except Exception as e:
        print(f"An error occurred: {e}")

input('Press Enter to close...')
driver.quit()