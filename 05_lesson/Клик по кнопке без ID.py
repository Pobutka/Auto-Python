from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


driver.get("http://uitestingplayground.com/classattr")

print("Page loaded. Waiting for button to be clickable...")

try:
    blue_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn-primary"))
    )
    print("Button found. Clicking...")
    blue_button.click()
    print("Button clicked successfully!")
except TimeoutException as e:
    print("TimeoutException occurred:", e)


driver.quit()
