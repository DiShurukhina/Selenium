import math
from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/find_link_text")

    lnk = str(math.ceil(math.pow(math.pi, math.e)*10000))
    link = browser.find_element_by_link_text(lnk)
    link.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

