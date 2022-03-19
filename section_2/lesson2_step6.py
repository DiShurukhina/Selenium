# Задание на execute_script
from selenium import webdriver
import math
import time

try:
    link = 'http://SunInJuly.github.io/execute_script.html'
    browser = webdriver.Chrome()
    browser.get(link)

    element = browser.find_element_by_id('input_value')
    x = element.text
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    button = browser.find_element_by_tag_name("button")
    # исполняется js-скрипт, который скроллит страницу до появления текстового поля для ввода значения
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()