# уникальность селекторов
from selenium import webdriver
import time
import unittest

link1 = "http://suninjuly.github.io/registration1.html"
link2 = "http://suninjuly.github.io/registration2.html"



# Создаем класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
class TestReg(unittest.TestCase):
    def test_registration1(self):
        browser = webdriver.Chrome()
        browser.get(link1)
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".third_class .third")
        input3.send_keys("Ivan@mamail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, 'test_registration1 failed')


    def test_registration2(self):
        browser = webdriver.Chrome()
        browser.get(link2)
        input1 = browser.find_element_by_css_selector(".first_block .first")
        input1.send_keys("Ivan")
        input2 = browser.find_element_by_css_selector(".first_block .second")
        input2.send_keys("Petrov")
        input3 = browser.find_element_by_css_selector(".third_class .third")
        input3.send_keys("Ivan@mamail.ru")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(5)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual ("Congratulations! You have successfully registered!", welcome_text, 'test_registration2 failed')

# Заменяем строку запуска программы на unittest.main()
if __name__ == '__main__':
    unittest.main()


# решение с вынесением повторяющегося кода в отдельную функцию.
# переделать потом свой тест

# from selenium import webdriver
# import time
# import unittest

# def fill_form(link):
#     browser = webdriver.Firefox()
#     browser.get(link)

#     browser.find_element_by_css_selector(".first:required").send_keys("Ivan")
#     browser.find_element_by_css_selector(".second:required").send_keys("Petrov")
#     browser.find_element_by_css_selector(".third:required").send_keys("url@gmail")
#     browser.find_element_by_css_selector("button.btn").click()
    
#     return browser.find_element_by_tag_name("h1").text

# class TestReg(unittest.TestCase):
#     def test_reg1(self):
#         self.assertEqual(fill_form("http://suninjuly.github.io/registration1.html"), "Congratulations! You have successfully registered!", "registration is failed")

#     def test_reg2(self):
#       self.assertEqual(fill_form("http://suninjuly.github.io/registration2.html"), "Congratulations! You have successfully registered!", "registration is failed")

# if __name__ == "__main__":
#     unittest.main()