from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()

try:
    
    driver.get("http://the-internet.herokuapp.com/login")

    
    username_field = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )
    username_field.send_keys("tomsmith")


    password_field = driver.find_element(By.NAME, "password")
    password_field.send_keys("SuperSecretPassword!")

    
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    
    WebDriverWait(driver, 10).until(
        EC.url_contains("secure")
    )

finally:
    
    driver.quit()
