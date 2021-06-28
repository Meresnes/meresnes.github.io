# Программирование (Python) Петров Роман Сергеевич
# 6 семестр, тема 1

# Лабораторная работа 1

"""
Используя обучающий набор данных о пассажирах Титаника, находящийся в проекте (оригинал: https://www.kaggle.com/c/titanic/data), найдите ответы на следующие вопросы: 

1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.

2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.

3. Посчитайте долю (процент) погибших на параходе (число и процент)?

4. Какие доли составляли пассажиры первого, второго, третьего класса?

5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).

6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:
1) возрастом и параметром survival;
2) полом человека и параметром survival;
3) классом, в котором пассажир ехал, и параметром survival.

7. Посчитайте средний возраст пассажиров и медиану.
8. Посчитайте среднюю цену за билет и медиану.

9. Какое самое популярное мужское имя на корабле?
10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?


Для вычисления 3, 4, 5, 6, 7, 8 используйте тип данных float с точностью два знака в дробной части. 


"""

import pandas  # импортирование библиотеки для считывания данных
import numpy as np

# считаем данных из файла, в качестве столбца индексов используем PassengerId
data = pandas.read_csv('train.csv', index_col="PassengerId")


# TODO #1
def get_sex_distrib(data):
    """
    1. Какое количество мужчин и женщин ехало на параходе? Приведите два числа через пробел.
    """

    n_male, n_female = 0, 0

    for x in data['Sex']:
        if x == 'male':
            n_male += 1
    else:
        n_female += 1

    return n_male, n_female


# TODO #2
def get_port_distrib(data):
    """  
    2. Подсчитайте сколько пассажиров загрузилось на борт в различных портах? Приведите три числа через пробел.
    """

    port_S, port_C, port_Q = 0, 0, 0

    for x in data['Embarked']:
        if x == 'S':
            port_S += 1
        if x == 'C':
            port_C += 1
        if x == 'Q':
            port_Q += 1

    return port_S, port_C, port_Q


# TODO #3
def get_surv_percent(data):
    """
    3. Посчитайте долю погибших на параходе (число и процент)?
    """

    n_died, perc_died = 0, 0
    n = 0
    for x in data['Survived']:
        n += 1
        if x == 1:
            n_died += 1

    perc_died = round((n_died / n * 100), 2)
    return n_died, perc_died


# TODO #4
def get_class_distrib(data):
    """
    4. Какие доли составляли пассажиры первого, второго, третьего класса?    
    """
    n_pas_f_cl, n_pas_s_cl, n_pas_t_cl = 0, 0, 0
    n = 891
    for x in data['Pclass']:
        if x == 1:
            n_pas_f_cl += 1
        if x == 2:
            n_pas_s_cl += 1
        if x == 3:
            n_pas_t_cl += 1

        n_pas_f_cl = round(n_pas_f_cl / n, 2)
        n_pas_s_cl = round(n_pas_s_cl / n, 2)
        n_pas_t_cl = round(n_pas_t_cl / n, 2)

    return n_pas_f_cl, n_pas_s_cl, n_pas_t_cl


# TODO #5
def find_corr_sibsp_parch(data):
    """
    5. Вычислите коэффициент корреляции Пирсона между количеством супругов (SibSp) и количеством детей (Parch).
    """

    corr_val = -1
    return corr_val


# TODO #6-1
def find_corr_age_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - возрастом и параметром survival;

    """

    Age_list = []
    Survived_list = []
    corr_val = -1

    for x in range(0, len(data)):
        a = data.iloc[x]['Age']
        b = data.iloc[x]['Survived']
        if a == float(a) and b == float(b):
            Age_list.append(a)
            Survived_list.append(b)

    corr_val = np.corrcoef(Age_list, Survived_list)
    return corr_val


# TODO #6-2
def find_corr_sex_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - полом человека и параметром survival;
    """

    Sex_list = []
    Survived_list = []
    corr_val = -1

    for x in range(0, len(data)):
        a = data.iloc[x]['Sex']
        b = data.iloc[x]['Survived']
        if a == float(a) and b == float(b):
            Sex_list.append(a)
            Survived_list.append(b)

    corr_val = np.corrcoef(Sex_list, Survived_list)
    return corr_val


# TODO #6-3
def find_corr_class_survival(data):
    """
    6. Выясните есть ли корреляция (вычислите коэффициент корреляции Пирсона) между:

    - классом, в котором пассажир ехал, и параметром survival.
    """

    corr_val = -1
    return corr_val


# TODO #7
def find_pass_mean_median(data):
    """
    7. Посчитайте средний возраст пассажиров и медиану.
    """

    mean_age, median = None, None

    AgeSumm = 0
    n = 0
    ExsistAge = []
    for x in data['Age']:
        try:
            AgeSumm += int(x)
            n += 1
            ExsistAge.append(x)

        except:
            pass

    mean_age = round(AgeSumm / n, 2)
    median = np.median(ExsistAge)

    return mean_age, median


# TODO #8
def find_ticket_mean_median(data):
    """
    8. Посчитайте среднюю цену за билет и медиану.
    """

    mean_price, median = 0, None
    n = 0
    PriceList = []
    for x in data['Fare']:
        PriceList.append(x)
        mean_price += x
        n += 1
    mean_price = round(mean_price / n, 2)
    median = round(np.median(PriceList), 2)

    return mean_price, median


# TODO #9
def find_popular_name(data):
    """
    9. Какое самое популярное мужское имя на корабле?
    """

    NameList = []

    z = -1
    for x in data['Name']:
        z += 1
        n = 0
        k = 0
        name = ''
        if data.iloc[z]['Sex'] == 'male':
            for j in x:
                if n == 1:
                    if j == ' ':
                        k += 1
                    if k < 2:
                        name += j

                if j == '.':
                    n = 1
            NameList.append(name.strip())

    array_d = {}.fromkeys(NameList, 0)
    for a in NameList:
        array_d[a] += 1

    k = -1
    for x in array_d:
        if array_d[x] > k:
            k = array_d[x]
            name = x

    return name


# TODO #10
def find_popular_adult_names(data):
    """
    10. Какие самые популярные мужское и женские имена людей, старше 15 лет на корабле?
    """
    popular_male_name, popular_female_name = "", ""
    return popular_male_name, popular_female_name


# ------------------------------

# Реализуем вычисление количества пассажиров на параходе и опишем предварительные действия с данными (считывание)

# После загрузки данных с помощью метода read_csv и индексации его по первому столбцу данных (PassangerId) становится доступно выборка данных по индексу. 
# С помощью запроса ниже мы можем получить имя сотого пассажира
print(type(data.iloc[100]))
print(data.iloc[100]['Sex'])

print((data['Name'], data['Sex']))


def get_number_of_pass(data_file):
    """
        Подсчет количества пассажиров. 
        data_file - str
        В качестве аргумента удобнее всего использовать строковую переменную, куда будет передаваться название файла (т. к. далее, возможно, потребуется подсчитать параметры для другого набора данных test.csv)
    """
    male_int, female_int = 0, 0
    # считывание и обработка данных
    data = pandas.read_csv(data_file, index_col="PassengerId")

    # считать данных из столбца возможно с помощью метода value_counts()
    res = data['Sex'].value_counts()
    # res будет содержать ассоциативный массив, ключами в котором являются значения столбца sex, а целочисленные значениями - количества пассажиров обоих полов
    male_int, female_int = res['male'], res['female']
    return male_int, female_int


def test_get_number_of_pass():
    assert get_number_of_pass('train.csv') == (577, 314), " Количество мужчин и женщин на Титанике"

# аналогично протестировать остальные функции