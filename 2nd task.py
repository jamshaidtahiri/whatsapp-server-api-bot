from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set the path to your Chrome user data directory
chrome_user_data_directory = "C:/Path/To/Your/Chrome/User/Data/Directory"

# Create Chrome options and set the user data directory
chrome_options = Options()
chrome_options.add_argument(f"--user-data-dir={chrome_user_data_directory}")

# Initialize WebDriver with Chrome options
driver = webdriver.Chrome(options=chrome_options)

# List of contacts to send messages to
contacts = ["+923102767334",  "+923000576678" , "+923442902910" , "+923420761147"]
for contact_num in contacts:
    # Open no contact app (if not already open)
    driver.get("https://nocontactapp.com/")

    # # Wait for the user to scan the QR code
    wait = WebDriverWait(driver, 120)  # Adjust the timeout as needed
    wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div[1]/form/input")))

    # Loop through the list of contacts and send messages

    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/form/input").send_keys(contact_num)
    driver.find_element(By.XPATH,"/html/body/div[2]/div[1]/form/button").click()
    driver.find_element(By.XPATH,"//*[@id='action-button']/span").click()
    wait = WebDriverWait(driver, 10)
    element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='fallback_block']/div/div/h4[2]/a/span")))
    element.click()

    time.sleep(2)  # Add a small delay for search results to load

    # Send a message
    wait = WebDriverWait(driver, 60)
    message_box = wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='main']/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p")))

    message_text = "Hello bro!"
    message_box.send_keys(message_text)
    message_box.send_keys(Keys.RETURN)
    time.sleep(2)
#  Close the WebDriver when done
driver.quit()

