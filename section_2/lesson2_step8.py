from selenium import webdriver
import math
import time
import os

try:
    link = 'http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Dinara')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Dinara')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('Dinara')
    # ищу кнопку загрузки файла
    button = browser.find_element_by_id('file')
    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test_upload.txt')    # добавляем к этому пути имя файла 
    button.send_keys(file_path)
    submit = browser.find_element_by_css_selector('button[type="submit"]')
    submit.click()
    

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()