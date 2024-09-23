import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link1 = 'https://suninjuly.github.io/selects1.html'
link2 = 'https://suninjuly.github.io/selects2.html'


def func(link):
    try:
        browser = webdriver.Chrome()
        browser.get(link)
        num1 = browser.find_element(By.ID, 'num1').text
        num2 = browser.find_element(By.ID, 'num2').text
        sum = str(int(num1)+int(num2))
        select = Select(browser.find_element(By.TAG_NAME, 'select'))
        select.select_by_value(sum)

        browser.find_element(By.CSS_SELECTOR, 'button.btn-default').click()

    finally:
        time.sleep(10)
        browser.quit()


func(link1)
func(link2)

