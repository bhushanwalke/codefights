__author__ = 'bhushan'

def fibo(n):
    if n == 0:
        return 0
    else:
        x1 = 0
        x2 = 1
        for i in range(2, n):
            x3 = x1+x2
            x1 = x2
            x2 = x3
        return x2


print(fibo(5))