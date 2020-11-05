import numpy as np
import sigfig
import random

def gera_dados(N, N_rep, x0, s0): #unidade em metros
    x = np.zeros((N_rep,N))
    n = np.zeros(N_rep)
    m = np.zeros(N_rep)
    for i in range(N_rep):
        for j in range(N):
            x[i][j] = random.gauss(x0,s0)
    xm = np.mean(x, axis=1)
    xM = np.median(x, axis=1)
    sx = np.std(x, axis=1)
    for i in range(N_rep):
        for j in range(N):
            if np.abs(x[i][j] - x0) <= s0:
                n[i]+=1
            if np.abs(x[i][j] - xm[i]) <= sx[i]:
                m[i]+=1
    return [xm,xM,sx,n,m]

func = gera_dados(100, 10000, 50, 1)

def a(f):
    xm = f[0]
    xM = f[1]
    sxm = np.std(xm)
    sxM = np.std(xM)
    z = (xm + xM)/2
    sz = np.std(z)
    print(f'a1) sxm = {sigfig.round(float(sxm),sigfigs=2)}, sxM = {sigfig.round(float(sxM),sigfigs=2)}')
    print(f'a2) sz = {sigfig.round(float(sz),sigfigs=2)}')
a(func)  

def b(f):
    n = f[3]
    m = f[4]
    n_m = np.mean(n)
    m_m = np.mean(m)
    sn_m = float(np.std(n)/np.sqrt(len(n)))
    sm_m = float(np.std(m)/np.sqrt(len(m)))
    print(f'b1) n = {n_m} +- {sigfig.round(sn_m, sigfigs=2)}, m = {m_m} +- {sigfig.round(sm_m, sigfigs=2)}')
    print(f'b3) sn_m = {sigfig.round(float(np.std(n)), sigfigs=2)}, sm_m = {sigfig.round(float(np.std(m)), sigfigs=2)}')
b(func)