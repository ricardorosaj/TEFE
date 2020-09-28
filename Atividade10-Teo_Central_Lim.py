import numpy as np

def func(x): return 3/2*x**2

N=10000
#------------------------------------------------------------------
#ITEM A
def metodo_exclusao_a(N, f):
    sigma_x = np.sqrt(3/5)
    xmin = -1
    xmax = 1
    ymax = 3/2
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1

    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in x:
            if np.abs(valor)<=lambdas[i]*sigma_x:
                ns[i]+=1
    return ns
print(f'N para cada lambda item a: {metodo_exclusao_a(N, func)}')

#-----------------------------------------------------------------------------------------
#ITEM B
def metodo_exclusao_b(N, f):
    sigma_x = np.sqrt(3/5)
    xmin = -1
    xmax = 1
    ymax = 3/2
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand_1 = xmin + (xmax - xmin) * np.random.rand()
        x_cand_2 = xmin + (xmax - xmin) * np.random.rand()
        x_cand = x_cand_1 + x_cand_2
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1

    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in x:
            if np.abs(valor)<=lambdas[i]*sigma_x:
                ns[i]+=1
    return ns
print(f'N para cada lambda item b: {metodo_exclusao_b(N, func)}')

#-----------------------------------------------------------------------
#ITEM C
def metodo_exclusao_c(M, N, f):
    xmin = -1
    xmax = 1
    ymax = 3/2
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand_1 = xmin + (xmax - xmin) * np.random.rand()
        x_cand_2 = xmin + (xmax - xmin) * np.random.rand()
        x_cand = x_cand_1 + x_cand_2
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1

    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in x:
            if np.abs(valor)<=lambdas[i]*sigma_x:
                ns[i]+=1
    return ns
print(f'N para cada lambda item c: {metodo_exclusao_b(3, N, func)}')
print(f'N para cada lambda item c: {metodo_exclusao_b(5, N, func)}')
print(f'N para cada lambda item c: {metodo_exclusao_b(10, N, func)}')
print(f'N para cada lambda item c: {metodo_exclusao_b(100, N, func)}')
 #--------------------------------------------------------------------------

#ITEM D
def metodo_exclusao_d(N, f):
    sigma_x = np.sqrt(3/5)
    xmin = -1
    xmax = 1
    ymax = 3/2
    i = 0
    x = np.zeros(N)
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1

    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in x:
            if np.abs(valor)<=lambdas[i]*sigma_x:
                ns[i]+=1
    return ns
print(f'N para cada lambda item d: {metodo_exclusao_d(N, func)}')