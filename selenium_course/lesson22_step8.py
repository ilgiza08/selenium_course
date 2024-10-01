import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/file_input.html'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("I")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("P")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("em")
    file_input = browser.find_element(By.CSS_SELECTOR, '[type="file"]')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_input.send_keys(file_path)

    submit = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(30)
    browser.quit()
    
