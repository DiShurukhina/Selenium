# ждем нужный текст на странице
# Explicit Waits (WebDriverWait и expected_conditions)
# Selenium Waits (Implicit Waits)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time


try:
    # открываю страницу
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/explicit_wait2.html'
    browser.get(link)

    # ищу кнопку для бронирования
    book = browser.find_element_by_id('book')
    # говорим Selenium ждать минимум 12 сек, пока цена не станет $100
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '$100')
        )
    book.click()
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()

finally:
    time.sleep(5)
    browser.quit()


