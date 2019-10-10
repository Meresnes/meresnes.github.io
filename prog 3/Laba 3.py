"""
Самостоятельная 3
Выполнил: Петров Роман
ИВТ 2 курс группа 1.1

"""
a = [0,0,1,1]
b = [0,1,0,1]
w = '|'
sp = ' '
print('-'*12)
print(w+sp*2+'A'+sp*2+w+sp*2+'B'+sp*2+w)
print('-'*12)
for i in range(4):
  print(w+sp*2+str(a[i])+sp*2+w+sp*2+str(b[i])+sp*2+w)
  print('-'*12)
