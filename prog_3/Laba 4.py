"""
Вычисление площали треугольника по формуле герона через функцию с проверкой
Сделал Петров Роман
Ивт 2 курс 1.1 группа
"""
import math

def geron_S(a,b,c):
    p = 0.5*(a + b + c)
    res = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return res

def main ():

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(geron_S(a,b,c))

if __name__ == "__main__":

    assert (geron_S(3, 4, 5) == 6)
    assert (geron_S(7, 8, 10) == 27.810744326608734)
    assert (geron_S(10, 12, 14) == 58.787753826796276)

    main()


