"""
Задание 2.1

Выполнил: Петров Роман
ИВТ 2 курс группа 1.1

"""
a = [0,0,1,1]
b = [0,1,0,1]

a1 = [0,0,0,1,0,1,1,1]
b1 = [0,0,1,0,1,1,0,1]
c1 = [0,1,0,0,1,0,1,1]

def log2(*args):
    
    if len(args) == 2:
        w = '|'
        sp = ' '
        print('-'*12)
        print(w+sp*2+'A'+sp*2+w+sp*2+'B'+sp*2+w+sp*2)
        print('-'*12)
        
        for i in range(4):
          print(w+sp*2+str(a[i])+sp*2+w+sp*2+str(b[i])+sp*2+w)
          print('-'*12)

          
    if len(args) == 3:
        w = '|'
        sp = ' '
        print('-'*18)
        print(w+sp*2+'A'+sp*2+w+sp*2+'B'+sp*2+w+sp*2+'C'+sp*2+w)
        print('-'*18)
        
        for i in range(8):
          print(w+sp*2+str(a1[i])+sp*2+w+sp*2+str(b1[i])+sp*2+w+sp*2+str(c1[i])+sp*2+w)
          print('-'*18)

i = int(input('Введите количество аргуменов (2 или 3):'))
if i == 2:
    log2(a,b)
if i == 3:
   log2(a1,b1,c1)
if (i != 2) & (i != 3):
    print('Вы ввели неправильные значения!')


