import random
import numpy as np

#Exercício 1
def tmc1(v_real, desv_pad, N):
    w = np.zeros(N)
    count_1s = 0
    count_2s = 0
    count_3s = 0
    for i in range(N):
        rand = random.gauss(0,1)
        x = v_real + desv_pad*rand
        w[i] = x
    xm = np.mean(w)
    std_x = np.std(w)    
    for i in range(len(w)):
        if w[i] > xm - std_x and w[i] < xm + std_x:
            count_1s += 1
        if w[i] > xm - 2*std_x and w[i] < xm + 2*std_x:
            count_2s += 1
        if w[i] > xm - 3*std_x and w[i] < xm + 3*std_x:
            count_3s += 1    
    print(f'''1.1) Valor médio de x: {xm}, Desvio padrão da média de x: {np.std(w)/np.sqrt(N)}
    1.2) Desvio padrão amostral de x: {std_x}
    1.3) x distante 1 sigma: {count_1s}
    1.4) x distante 2 sigma: {count_2s}
    1.5) x distante 3 sigma: {count_3s}\n''')
    
tmc1(0, 1, 10000)

#Exercício 2
def tmc2(N):
    w = np.zeros(N)
    count_1s = 0
    count_2s = 0
    count_3s = 0
    for i in range(N):
        rand = np.random.uniform(-0.5, 0.5)
        y = rand
        w[i] = y
    ym = np.mean(w)
    std_y = np.std(w)    
    for i in range(len(w)):
        if w[i] > ym - std_y and w[i] < ym + std_y:
            count_1s += 1
        if w[i] > ym - 2*std_y and w[i] < ym + 2*std_y:
            count_2s += 1
        if w[i] > ym - 3*std_y and w[i] < ym + 3*std_y:
            count_3s += 1    
    print(f'''2.1) Valor médio de y: {ym}, Desvio padrão da média de y: {np.std(w)/np.sqrt(N)}
    2.2) Desvio padrão amostral de y: {std_y}
    2.3) y distante 1 sigma: {count_1s}
    2.4) y distante 2 sigma: {count_2s}
    2.5) y distante 3 sigma: {count_3s}\n''')

tmc2(10000)

#Exercício 3
def tmc3(N):
    w = np.zeros(N)
    count_1s = 0
    count_2s = 0
    count_3s = 0
    for i in range(N):
        rand1 = np.random.uniform(-0.5, 0.5)
        rand2 = np.random.uniform(-0.5, 0.5)
        z = rand1 + rand2
        w[i] = z
    zm = np.mean(w)
    std_z = np.std(w)    
    for i in range(len(w)):
        if w[i] > zm - std_z and w[i] < zm + std_z:
            count_1s += 1
        if w[i] > zm - 2*std_z and w[i] < zm + 2*std_z:
            count_2s += 1
        if w[i] > zm - 3*std_z and w[i] < zm + 3*std_z:
            count_3s += 1    
    print(f'''3.1) Valor médio de z: {zm}, Desvio padrão da média de z: {np.std(w)/np.sqrt(N)}
    3.2) Desvio padrão amostral de z: {std_z}
    3.3) z distante 1 sigma: {count_1s}
    3.4) z distante 2 sigma: {count_2s}
    3.5) z distante 3 sigma: {count_3s}\n''')

tmc3(10000)    