from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PIL import Image, ImageOps
from selenium.webdriver.chrome.options import Options

import base64


def generate_qr_code_image(number):
    options = Options()
    chrome_user_data_directory = fr"C:/Users/MR MJT/Desktop/{number}"

    options.add_argument(f"--user-data-dir={chrome_user_data_directory}")
    driver = webdriver.Chrome(options=options)

    # Open WhatsApp Web
    driver.get("https://web.whatsapp.com/")

    # Wait for the QR code to appear
    wait = WebDriverWait(driver, 60)  # Adjust the timeout as needed
    qr_code = wait.until(EC.presence_of_element_located((By.XPATH, "//canvas[@aria-label='Scan me!']")))

    # Take a screenshot of the QR code
    qr_code.screenshot("qr_code_screenshot.png")

    # Close the browser when done
    driver.quit()

    # Open the screenshot using Pillow
    image = Image.open("qr_code_screenshot.png")

    # Define the desired white space size (in pixels) around the QR code
    padding = 20

    # Add white space around the QR code
    image_with_padding = ImageOps.expand(image, padding, (255, 255, 255))

    # Save the modified image
    image_with_padding.save("qr_code_screenshot_with_padding.png")

    
    # Encode the modified image as base64
    with open("qr_code_screenshot_with_padding.png", "rb") as qr_file:
        qr_bytes = qr_file.read()
        return base64.b64encode(qr_bytes).decode('utf-8')