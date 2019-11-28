"""
Задача 2.4
Вариант №7
Выполнил Петров Роман 1.1
"""
import math
def square(v):
    s = v**(1/3)
    s = int(s**2 * 6)
    print('s =',s)
    return s
if __name__ == '__main__':
    assert square(8) == 24,'при V = 8 правильный ответ не получен'
    assert square(27) == 54,'при V = 27 правильный ответ не получен'
    assert square(64) == 95,'при V = 64 правильный ответ не получен'
