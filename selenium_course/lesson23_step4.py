import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
    browser.switch_to.alert.accept()

    y = calc(browser.find_element(By.ID, 'input_value').text)
    browser.find_element(By.ID, 'answer').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, 'button.btn').click()
finally:
    time.sleep(30)
    browser.quit()
    