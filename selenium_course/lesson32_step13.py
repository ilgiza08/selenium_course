from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"


class TestLogin(unittest.TestCase):
    def test_login1(self):
        browser = webdriver.Chrome()
        browser.get(link1)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        first_name.send_keys('I')
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        last_name.send_keys('L')
        email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        email.send_keys("e")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error!")

    def test_login2(self):
        browser = webdriver.Chrome()
        browser.get(link2)

        first_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.first")
        first_name.send_keys('I')
        last_name = browser.find_element(By.CSS_SELECTOR, ".first_block input.second")
        last_name.send_keys('L')
        email = browser.find_element(By.CSS_SELECTOR, ".first_block input.third")
        email.send_keys("e")

        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        time.sleep(1)
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Error!")


if __name__ == "__main__":
    unittest.main()