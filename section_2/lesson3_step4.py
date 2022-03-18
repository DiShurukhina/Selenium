from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/alert_accept.html'
    browser.get(link)

    # ищу кнопку для открытия alert-окна
    input1 = browser.find_element_by_css_selector('.container button[type="submit"]')
    input1.click()
    # ищу alert и жму там кнопку
    alert = browser.switch_to.alert
    alert.accept()   
    # вычисляю значение
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
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()