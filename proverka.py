from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

try:
    link = "http://suninjuly.github.io/registration2.html"
    driver.get(link)

    first_name = driver.find_element(By.XPATH, '//*[contains(@placeholder, "first")]')
    first_name.send_keys('name')
    last_name = driver.find_element(By.XPATH, '//*[contains(@placeholder, "last")]')
    last_name.send_keys('lastname')
    email = driver.find_element(By.XPATH, '//*[contains(@placeholder, "email")]')
    email.send_keys('email')
    button = driver.find_element(By.XPATH, "//*[text()='Submit']")
    button.click()
    time.sleep(1)

    welcome_text_elt = driver.find_element(By.XPATH, '//h1')
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    driver.quit()