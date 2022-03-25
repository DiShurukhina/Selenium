# переход на новую вкладку
from selenium import webdriver
import time
import math

try:
    browser = webdriver.Chrome()
    link = 'http://suninjuly.github.io/redirect_accept.html'
    browser.get(link)


    #жму кнопку для перехода на новую вкладку
    trollface = browser.find_element_by_class_name('trollface')
    trollface.click()
    # перехожу на новую вкладку
    first_window = browser.window_handles[0]
    new_window = browser.window_handles[1]
    browser.switch_to_window(new_window)
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
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()