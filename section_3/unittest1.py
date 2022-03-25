# Для unittest существуют собственные дополнительные правила:
# Тесты обязательно должны находиться в специальном тестовом классе.
# Вместо assert должны использоваться специальные assertion методы.

# Изменяем наши предыдущие тесты из файла test_abs_project.py, чтобы их можно было запустить с помощью unittest
import unittest

# Создаем класс, который должен наследоваться от класса TestCase: class TestAbs(unittest.TestCase):
class TestAbs(unittest.TestCase):
# Превращаем тестовые функции в методы, 
# добавив ссылку на экземпляр класса self в качестве первого аргумента функции: def test_abs1(self):
    def test_abs1(self):
        self.assertEqual(abs(-42), 42, "Should be absolute value of a number") # Изменяем assert на self.assertEqual()
    
    def test_abs2(self):
        self.assertEqual(abs(-42), -42, "Should be absolute value of a number")

# Заменяем строку запуска программы на unittest.main()
if __name__ == '__main__':
    unittest.main()
