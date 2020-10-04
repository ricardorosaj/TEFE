import pandas as pd
import numpy as np

#1 e 2 são dados teóricos
dict_data = {'1':[0.00800, 0.05600, 0.15200, 0.29600, 0.48800],
'2':[1.60, 11.20, 30.40, 59.20, 97.60],
'3':[], '4':[], '5':[], '6':[], '7':[], '8':[]}

def func(x): return 3/125*x**2

def metodo_exclusao(N, f):
    xmin = 0
    xmax = 5
    ymax = 0.6
    i = 0
    x = np.zeros(N)
    cont_0_1 = 0
    cont_1_2 = 0
    cont_2_3 = 0
    cont_3_4 = 0
    cont_4_5 = 0
    while i < N:
        x_cand = xmin + (xmax - xmin) * np.random.rand()
        y_test = ymax * np.random.rand()
        if y_test <= f(x_cand):
            x[i] = x_cand
            i += 1
    for i in range(len(x)):
        if 0 <= x[i] < 1:
            cont_0_1+=1
        if 1<= x[i] < 2:
            cont_1_2+=1
        if 2 <= x[i] < 3:
            cont_2_3+=1
        if 3 <= x[i] < 4:
            cont_3_4+=1
        if 4 <= x[i] < 5:
            cont_4_5+=1                    
    return [cont_0_1, cont_1_2, cont_2_3, cont_3_4, cont_4_5]

def metodo_exclusao_com_matriz(M, N, f): #M=10000 e N=200
    xmin = 0
    xmax = 5
    ymax = 0.6
    x = np.zeros((N,M))
    for j in range(M):
        i = 0
        while i < N:
            x_cand = xmin + (xmax - xmin) * np.random.rand()
            y_test = ymax * np.random.rand()
            if y_test <= f(x_cand):
                x[i][j] = x_cand
                i += 1
    lista_0_1 = []
    lista_1_2 = []
    lista_2_3 = []
    lista_3_4 = []
    lista_4_5 = []
    for i in range(len(x)):
        cont_0_1 = 0
        cont_1_2 = 0
        cont_2_3 = 0
        cont_3_4 = 0
        cont_4_5 = 0
        for j in range(len(x[i])):
            if 0 <= x[i][j] < 1:
                cont_0_1+=1
            if 1<= x[i][j] < 2:
                cont_1_2+=1
            if 2 <= x[i][j] < 3:
                cont_2_3+=1
            if 3 <= x[i][j] < 4:
                cont_3_4+=1
            if 4 <= x[i][j] < 5:
                cont_4_5+=1
        lista_0_1.append(cont_0_1)       
        lista_1_2.append(cont_1_2)
        lista_2_3.append(cont_2_3)
        lista_3_4.append(cont_3_4)
        lista_4_5.append(cont_4_5)
    med_0_1 = np.mean(lista_0_1)
    mean_std_0_1 = np.std(lista_0_1)/np.sqrt(len(lista_0_1))
    std_0_1 = np.std(lista_0_1)
    med_1_2 = np.mean(lista_1_2)
    mean_std_1_2 = np.std(lista_1_2)/np.sqrt(len(lista_1_2))
    std_1_2 = np.std(lista_1_2)
    med_2_3 = np.mean(lista_2_3)
    mean_std_2_3 = np.std(lista_2_3)/np.sqrt(len(lista_2_3))
    std_2_3 = np.std(lista_2_3)
    med_3_4 = np.mean(lista_3_4)
    mean_std_3_4 = np.std(lista_3_4)/np.sqrt(len(lista_3_4))
    std_3_4 = np.std(lista_3_4)
    med_4_5 = np.mean(lista_4_5)
    mean_std_4_5 = np.std(lista_4_5)/np.sqrt(len(lista_4_5))
    std_4_5 = np.std(lista_4_5)
    return [[med_0_1, mean_std_1_2, med_2_3, med_3_4, med_4_5],[mean_std_0_1, mean_std_1_2, mean_std_2_3, mean_std_3_4, mean_std_4_5]
    ,[std_0_1, std_1_2, std_2_3, std_3_4, std_4_5]]

c1 = metodo_exclusao(200, func)
c2 = metodo_exclusao(200, func)
c3 = metodo_exclusao(200, func)
d = metodo_exclusao_com_matriz(10000, 200, func)

dict_data['3']=c1
dict_data['4']=c2
dict_data['5']=c3
dict_data['6']=d[0]
dict_data['7']=d[1]
dict_data['8']=d[2]

pd.DataFrame.from_dict(dict_data).to_csv('atividade11.csv', sep='\t', index=False)