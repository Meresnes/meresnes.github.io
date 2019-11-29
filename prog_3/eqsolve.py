import math

def discr(a=0, b=0, c=0, accuracy=0.00001):

    res = b**2 - 4*a*c
    return float(res)

def solve_eq(a, b, c, accuracy=0.00001):
    
    x1, x2 = None, None
    
    d = discr(a,b,c,accuracy)
    

    
    if d > 0:    
        d = float(math.sqrt(d))
        x1 = float('{0:.{w}f}'.format((-b + d) / (2 * a), accuracy))
        x2 = float('{0:.{w}f}'.format((-b - d) / (2 * a), accuracy))

        return (x1, x2)
    elif d == 0 and a != 0:
         return float('{0:.{w}f}'.format((-b) / (2 * a), accuracy))
    elif d < 0:
        return x1, x2
        


assert solve_eq(1,2,3) == (None, None),  "Значение по умолчанию для заглушки функции"

# 1 test case = тестовый случай 
discr(1)  # 0

# 2 
discr(1, c=1/4) # -1.0 

# 3
discr(1,b=2,c=1/4) # 3.0 

# 4
discr(1,b=2,c=3) # -8.0

# 5
discr()  # 0.0

# 5
discr()  # 0.0

# 6
discr()

# 7 
res7 = discr(a=0.0005, b=1.0000043, c=5.00000003339992)

if __name__ == '__main__':
    
    def test1(*inpvals):
        print('test1 is running')
        try:
            assert res7 == 0.99 , "Ошибка при определении точности вычислений"
        except AssertionError as e:
            print(f"ошибка была такая: {e} при таких-то значениях {inpvals[0]}")

    def test2():
        print('test2 is running')
        try:
            assert res7 == 0.9900085999516904 , "Ошибка при определении точности вычислений"
        except AssertionError as e:
            print(f"ошибка была такая: {e}")


    test1()
    test2()
