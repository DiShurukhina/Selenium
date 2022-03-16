from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/selects1.html"
    browser.get(link)

    #ищу числа
    num1 = browser.find_element_by_id("num1")
    num2 = browser.find_element_by_id("num2")
    num1, num2 = num1.text, num2.text
    summ = 0
    # ищу сумму
    def calc(summ):
        return str(int(num1) + int(num2))
    x = calc(summ)
    # ищу сумму в выпадающем списке
    select = Select(browser.find_element_by_class_name("custom-select"))
    select.select_by_value(x) # ищем элемент с текстом , равным summ
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()


finally:
    time.sleep (10)
    browser.quit()