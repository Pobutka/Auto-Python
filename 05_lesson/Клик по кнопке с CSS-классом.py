from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Create a new instance of the Chrome options
options = Options()

# Bypass SSL errors
options.add_argument("--accept-insecure-certs")

# Create a new instance of the Chrome driver with the options
driver = webdriver.Chrome(options=options)

# Open the page
driver.get("http://uitestingplayground.com/classattr")

# Find the blue button by its CSS class
blue_button = driver.find_element(By.CSS_SELECTOR, "button.btn-primary")

# Use JavaScript to click on the blue button
driver.execute_script("arguments[0].click();", blue_button)

# Close the browser
driver.quit()

