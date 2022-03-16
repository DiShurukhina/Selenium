from selenium import webdriver
import math
import time

link = "http://suninjuly.github.io/get_attribute.html"
browser = webdriver.Chrome()
browser.get(link)

# ищу картинку с сундучком
treasure = browser.find_element_by_id("treasure")
x = treasure.get_attribute("valuex")
print (x)
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))
y = calc(x)
print("value of people radio: ", y)
