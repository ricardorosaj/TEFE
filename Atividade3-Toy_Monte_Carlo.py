import numpy as np
import random

def func1(r):
    return np.pi*r**2

def func2(d):
    return d**3

def func3(a,b):
    return a/b

def func3b(a):
    return a/20.0

def func3c(b):
    return 10.0/b

def toy_monte_carlo(v_real, desv_pad ,funcao, N):
    w = np.zeros(N)
    for i in range(N):
        x = v_real + desv_pad*random.gauss(0,1)
        w[i] = funcao(x)
    print(f'Incerteza:{np.std(w)}\nValor médio:{np.mean(w)}\nIncerteza do valor médio:{np.std(w)/np.sqrt(N)}\n')

def toy_monte_carlo2(v_real1, desv_pad1, v_real2, desv_pad2,funcao, N):
    w = np.zeros(N)
    for i in range(N):
        x = v_real1 + desv_pad1*random.gauss(0,1)
        y = v_real2 + desv_pad2*random.gauss(0,1)
        w[i] = funcao(x,y)
    print(f'Incerteza:{np.std(w)}\nValor médio:{np.mean(w)}\nIncerteza do valor médio:{np.std(w)/np.sqrt(N)}\n')

N=10000
toy_monte_carlo(15.0, 1.0, func1, N) #1
toy_monte_carlo(5.0, 1.0, func2, N) #2
toy_monte_carlo2(10.0, 2.0, 20.0, 2.0, func3, N) #3
toy_monte_carlo(10.0, 2.0, func3b,N) #3b
toy_monte_carlo(20.0, 2.0, func3c,N) #3c