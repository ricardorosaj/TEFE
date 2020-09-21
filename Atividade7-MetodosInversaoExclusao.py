import numpy as np

#define metodo de exclusão para exercício 1
def metodo_exclusao(N):
    xmin = -1
    xmax = 1
    ymax = 3/4
    f = lambda x : 3/4*(1-x**2)
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

ex1 = metodo_exclusao(10000)
print(f'''1-a) Média de x {np.mean(ex1[0])} com incerteza {np.std(ex1[0])/np.sqrt(10000)}
1-b) Desv pad amostral: {np.std(ex1[0])}
1-c) Dados dentro de 1 sigma {ex1[1]} e frequência relativa {ex1[2]}''')

#define metodo de inversão para exercício 2
def metodo_inversao(N):    
    inv_g = lambda g : 1/2*np.arccos(g)
    # gera N valores de g com distribuicao uniforme entre 0 e 1
    g = np.random.rand(N)
    # calcula os valores de x correspondentes
    x = inv_g(g)

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

ex2 = metodo_inversao(10000)
print(f'''2-a) Média de x {np.mean(ex2[0])} com incerteza {np.std(ex2[0])/np.sqrt(10000)}
2-b) Desv pad amostral: {np.std(ex2[0])}
2-c) Dados dentro de 1 sigma {ex2[1]} e frequência relativa {ex2[2]}''')