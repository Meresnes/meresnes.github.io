"""
Организовать вывод суммы чисел от 1 до 50
Сделал Петров Роман
Ивт 2 курс 1.1 группа
"""

def SUMM():
    res = 0
    for arg in range(1,51):
        res += arg
    return res
print('Sum = {}'.format(SUMM()))
