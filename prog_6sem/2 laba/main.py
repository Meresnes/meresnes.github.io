
import pandas  # импортирование библиотеки для считывания данных
from collections import Counter
import numpy as np
import matplotlib.pyplot as plt
# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")

Age_list = []
Survived_list = []
corr_val = -1

for x in range(0,len(data)):
    a = data.iloc[x]['Age']
    b = data.iloc[x]['Survived']
    if a == float(a) and b == float(b):
        Age_list.append(a)
        Survived_list.append(b)


corr_val = np.corrcoef(Age_list, Survived_list)
print(corr_val)


# and isinstance((float(data.iloc[x]['Survived'])), float)