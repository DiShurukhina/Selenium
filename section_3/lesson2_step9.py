# Задание: составные сообщения об ошибках
# Вам дана функция test_input_text,  которая принимает два значения: 
# expected_result — ожидаемый результат, и actual_result — фактический результат. 
# Обратите внимание, input использовать не нужно!
# Функция должна проверить совпадение значений с помощью оператора assert и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 

def test_input_text(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'

# Задание: составные сообщения об ошибках и поиск подстроки
# Вам дан шаблон для функции test_substring, которая принимает два значения: full_string и substring. 
# Функция должна проверить вхождение строки substring в строку full_string с помощью оператора assert
# и, в случае несовпадения, предоставить исчерпывающее сообщение об ошибке. 

def test_substring(full_string, substring):
    # ваша реализация, напишите assert и сообщение об ошибке
    assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"