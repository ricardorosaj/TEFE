import numpy as np
import pandas as pd

dict_data = {'item a':0, 'item b':0, 'M=3':0, 'M=5':0, 'M=10':0, 'M=100':0, 'item d':0}

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
item_a = metodo_exclusao_a(N, func)
print(f'N para cada lambda item a: {item_a}')
dict_data['item a']=item_a

#-----------------------------------------------------------------------------------------
#ITEM B
def metodo_exclusao_b(M, N, f):
    xmin = -1
    xmax = 1
    ymax = 3/2
    x = np.zeros((N,M))
    for j in range(M):
        i = 0
        while i < N:
            x_cand = xmin + (xmax - xmin) * np.random.rand()
            y_test = ymax * np.random.rand()
            if y_test <= f(x_cand):
                x[i][j] = x_cand
                i += 1
    #print(x)            
    y = np.sum(x, axis=1)      
    sigma_y = np.std(y)
    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in y:
            if np.abs(valor)<=lambdas[i]*sigma_y:
                ns[i]+=1
    return ns
item_b = metodo_exclusao_b(2, N, func)
print(f'N para cada lambda item b: {item_b}')
dict_data['item b'] = item_b

#-----------------------------------------------------------------------
#ITEM C
def metodo_exclusao_c(M, N, f):
    xmin = -1
    xmax = 1
    ymax = 3/2
    x = np.zeros((N,M))
    for cont in range(M):
        i = 0
        while i < N:
            x_cand = xmin + (xmax - xmin) * np.random.rand()
            y_test = ymax * np.random.rand()
            if y_test <= f(x_cand):
                x[i][cont] = x_cand
                i += 1
    S = np.sum(x, axis=1)      
    sigma_S = np.std(S)
    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in S:
            if np.abs(valor)<=lambdas[i]*sigma_S:
                ns[i]+=1
    return ns

M3 = metodo_exclusao_c(3, N, func)
M5 = metodo_exclusao_c(5, N, func)
M10 = metodo_exclusao_c(10, N, func)
M100 = metodo_exclusao_c(100, N, func)
print(f'N para cada lambda item c com M=3: {M3}')
print(f'N para cada lambda item c com M=5: {M5}')
print(f'N para cada lambda item c com M=10: {M10}')
print(f'N para cada lambda item c com M=100: {M100}')
dict_data['M=3']=M3
dict_data['M=5']=M5
dict_data['M=10']=M10
dict_data['M=100']=M100

 #--------------------------------------------------------------------------

#ITEM D
def randn_d(N):
    x = np.random.randn(N)
    sigma_z = np.std(x)
    ns = [0, 0, 0, 0, 0]
    lambdas = [1, 1.5, 2, 2.5, 3]
    for i in range(len(lambdas)):        
        for valor in x:
            if np.abs(valor)<=lambdas[i]*sigma_z:
                ns[i]+=1
    return ns
item_d = randn_d(N)    
print(f'N para cada lambda item d: {item_d}')
dict_data['item d']=item_d

pd.DataFrame.from_dict(dict_data).to_csv('atividade10_certo.csv', index=False, header=False, sep='\t')