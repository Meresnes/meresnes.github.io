#import unittest
def game_1():
    #Игровое поле 3 на 3 
    matrix = [[' ' for x in range (3)] for x in range (3)]
    i = 0
    j = 0
    for string in matrix:
        i += 1
        for element in string:
            j += 1
            try:
                print('Строка № ' + i + ', элемент № ' + j)
                element = input('Введите X , O или пробел ')
