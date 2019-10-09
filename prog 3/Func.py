import math

def geron_S(a,b,c):
    p = a + b + c
    res = math.sqrt(p*(p-a)*(p-b)*(p-c))
    return res 
def main ():

    a = float(input("a = "))
    b = float(input("b = "))
    c = float(input("c = "))

    print(geron_S(a,b,c))

if __name__ == "__main__":
      main()
      
