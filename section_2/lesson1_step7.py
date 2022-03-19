# поиск сокровища с помощью get_attribute
from selenium import webdriver
import math
import time

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    # ищу картинку с сундучком
    treasure = browser.find_element_by_id("treasure")
    # получаю значение атрибута 
    x = treasure.get_attribute("valuex")
    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
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