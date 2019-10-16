import numpy as np

def percentel():
    n = int(input("Введите кол-во продавцов:"))
    p = int(input("Введите перцентель:"))
    x = (n+1)*(p/100)
    print('Percent: ',x)
    return x


a = [16, 12, 15, 15, 13, 14, 14, 21, 15, 23, 9, 15, 13, 14, 14, 21, 15, 14, 17, 27, 15, 13, 12, 16, 19, 14, 16, 17, 13, 14, 14]

"""while True:

   try:
       k = int(input(">>>"))
   except (ValueError):
       break

   a.append(k)
"""

print(a)

p = np.percentile(a, 25)
print(p)
