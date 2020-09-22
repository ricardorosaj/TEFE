import numpy as np
import random

#Exercício 1
def func1(x):
    return np.sin(np.deg2rad(x))

def tmc1(v_real, desv_pad, N, funcao):
    w = np.zeros(N)
    for i in range(len(w)):
        rand = random.gauss(0,1)
        x = v_real + desv_pad*rand
        w[i] = funcao(x)
    print(f'1- Incerteza de x: {np.std(w)}\nValor médio de x: {np.mean(w)}\nIncerteza no valor médio de x: {np.std(w)/np.sqrt(N)}\n')

tmc1(85.0, 10.0, 10000, func1)

#Exercício 2
def tmc2(v_real, desv_pad_aleat, desv_pad_sist, N, M):
    guarda_xf = np.zeros(M)
    conta_b = 0
    conta_c = 0
    for i in range(M):
        x = np.zeros(N)
        erro_sist = desv_pad_sist*random.gauss(0,1)
        for j in range(N):
            erro_aleat = desv_pad_aleat*random.gauss(0,1)
            x[j] = v_real + erro_aleat + erro_sist
        xf = np.mean(x)
        guarda_xf[i] = xf
        if xf > v_real:
            conta_b += 1
    sigma_f = np.std(guarda_xf)
    for i in range(M):
        if abs(guarda_xf[i] - v_real) < sigma_f:
            conta_c += 1
    print(f'2- a) Incerteza sigma_f: {sigma_f}\nb) Número de repetições b: {conta_b}\nc) Número de repetições c: {conta_c}\n')

tmc2(100, 28, 3, 50, 10000)

#Exercício 3
def func3(t):
    return 2*34.0/(t**2)

def tmc3(v_real, desv_pad, N, M, funcao):
    guarda_funcao = np.zeros(M)
    conta_b_1 = 0
    conta_b_2 = 0
    v_verdadeiro = funcao(v_real)
    for i in range(M):
        t = np.zeros(N)
        for j in range(N):
            erro_aleat = desv_pad*random.gauss(0,1)
            t[j] = v_real + erro_aleat
        tf = np.mean(t)
        guarda_funcao[i] = funcao(tf)  
    sigma_a = np.std(guarda_funcao)
    for i in range(M):
        if guarda_funcao[i] > v_verdadeiro:
            conta_b_1 += 1
        if abs(guarda_funcao[i] - v_verdadeiro) < sigma_a:
            conta_b_2 += 1
    print(f'3- a) Sigma_a: {sigma_a}\nb) Número de repetições 1: {conta_b_1} / Número de repetições 2: {conta_b_2}\n')

tmc3(2.525, 0.15, 287, 10000, func3)

#Exercício 4
func4 = func3

def tmc4(v_real, desv_pad, N, M, funcao):
    guarda_acel = np.zeros(M)
    conta_b_1 = 0
    conta_b_2 = 0
    v_verdadeiro = funcao(v_real)
    for i in range(M):
        t = np.zeros(N)
        acel = np.zeros(N)
        for j in range(N):
            erro_aleat = desv_pad*random.gauss(0,1)
            t[j] = v_real + erro_aleat
            acel[j] = funcao(t[j])
        acel_f = np.mean(acel)
        guarda_acel[i] = acel_f
    sigma_a = np.std(guarda_acel)
    for i in range(M):
        if guarda_acel[i] > v_verdadeiro:
            conta_b_1 += 1
        if abs(guarda_acel[i] - v_verdadeiro) < sigma_a:
            conta_b_2 += 1
    print(f'4- a) Sigma_a: {sigma_a}\nb) Número de repetições 1: {conta_b_1} / Número de repetições 2: {conta_b_2}')

tmc4(2.525, 0.15, 287, 10000, func4)    