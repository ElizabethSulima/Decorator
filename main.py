import os
from datetime import datetime

def logger(old_function):

    def new_function(*args, **kwargs):
        path = 'main.log'

        with open(path, 'a', encoding='utf-8') as log_file:
            log_file.write(
                f'{datetime.now()} - функция {old_function.__name__} вызвана с аргументами {args}, {kwargs}\n')
            result = old_function(*args, **kwargs)
            log_file.write(f'{datetime.now()} - функция {old_function.__name__} возвращает {result}\n')
        return result

    return new_function


def test_1():
    path = 'main.log'
    if os.path.exists(path):
        os.remove(path)

    @logger
    def hello_world():
        return 'Hello World'

    @logger
    def summator(a, b=0):
        return a + b

    @logger
    def div(a, b):
        return a / b

    result1 = hello_world()
    result2 = summator(2, 2)
    result3 = div(6, 2)

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
