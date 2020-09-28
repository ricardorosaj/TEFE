import numpy as np

def func1(x):
    return 3/4*(1-np.abs(x)**1) #mudar para cada valor de G (A=G+1/2G)

def metodo_exclusao(N, f):
    xmin = -1
    xmax = 1
    ymax = 3/4 #mudar sempre para o valor de A
    i = 0
    x = np.zeros(N)
    while i < N:
        # gera um possivel x com distribuicao uniforme entre xmim e mxmax
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        # gera um valor de y para comparacao com a PDF no ponto x gerado
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    xmean = np.mean(x)
    stdx = np.std(x)
    dif = xmean - stdx
    soma = xmean + stdx
    n = 0        
    for i in range(len(x)):
        if x[i] >= dif and x[i] <= soma:
            n+=1
    F = n/N        
    return [x,n,F]

N=1000

ex1 = metodo_exclusao(N, func1)
print(f'''1-a) Média de x {np.mean(ex1[0])} com incerteza {np.std(ex1[0])/np.sqrt(N)}
1-b) Desv pad amostral: {np.std(ex1[0])}
1-c) Dados dentro de 1 sigma {ex1[1]} e frequência relativa {ex1[2]}''')