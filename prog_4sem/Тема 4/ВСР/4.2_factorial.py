import unittest

def factorial(n):
    if n == 0:
        return 1
    try:
        return factorial(n-1)*n
    except(ValueError):
        print('Вы ввели неправильные данные')
        return 'Error'
    except (TypeError):
        print('Неверный тип данных')
    except:
        print('Ошибка!')
        return 'Error'
    
def input_test():
    
    try:
       x = int(input('Введите число:'))
       f = factorial(x)
       print(f)
       return f
    except(ValueError):
        print('Вы ввели неправильные данные')
    except(TypeError):
        print('Вы ввели неправильные данные')
    except:
        print('Ошибка')
class Test_factorial(unittest.TestCase):

    def test_1(self):
        self.assertEqual(factorial(5), 120)

    def test_2(self):
        self.assertEqual(factorial(5), 10)

    def test_3(self):
        self.assertEqual(factorial(1), 1)

    def test_4(self):
        self.assertEqual(factorial(3), 6)

    def test_5(self):
        self.assertEqual(factorial(das), 6)    
input_test()     

        
if __name__ == "__main__":
    unittest.main()
        
