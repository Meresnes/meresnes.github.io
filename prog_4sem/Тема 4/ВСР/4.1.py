def game_1():
    #Игровое поле 3 на 3 
    matrix = [[' ' for x in range (3)] for x in range (3)]
    string = 0
    element = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print('Строка:{}  Элемент:{}'.format(i,j))
            matrix[i][j] = input('Введите x , o или Enter')
    return matrix
print(game_1())

def game_test(matrix):
    '''
    Testing
    >>>game_1()
    '''
    pass
