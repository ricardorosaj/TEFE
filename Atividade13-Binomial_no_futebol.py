import pandas as pd
import numpy as np
from math import factorial

fut = pd.read_excel('new_leagues_data.xlsx', sheet_name='NOR')

def sig(N, p): return np.sqrt(N*p*(1-p))

def fdp_empate(n, p): return (factorial(10)/(factorial(n)*factorial(10-n)))*(p**10)*((1-p)**(10-n))

#1-
N_jogos = len(fut)
print(N_jogos)

nh = 0
na = 0
nd = 0
for i in range(N_jogos):
    if fut['HG'][i] > fut['AG'][i]:
        nh+=1
    if fut['HG'][i] < fut['AG'][i]:
        na+=1
    if fut['HG'][i] == fut['AG'][i]:
        nd+=1

fh = nh/N_jogos
fa = na/N_jogos
fd = nd/N_jogos

sig_nh = sig(N_jogos, fh)
sig_na = sig(N_jogos, fa)
sig_nd = sig(N_jogos, fd)

sig_fh = sig_nh/N_jogos
sig_fa = sig_na/N_jogos
sig_fd = sig_nd/N_jogos

p2_0 = fdp_empate(0, fd)
p2_1 = fdp_empate(1, fd)
p2_2 = fdp_empate(2, fd)
soma_fdp_p2 = p2_0+p2_1+p2_2

p10 = fdp_empate(10, fd)

print(f'2a - nh:{nh}, sigma_nh:{sig_nh}  2b - fh:{fh}, sigma_fh:{sig_fh}')
print(f'3 - na{na}, sigma_na:{sig_na}, fa:{fa}, sigma_fa:{sig_fa}')
print(f'4 - nd:{nd}, sigma_nd:{sig_nd}, fd:{fd}, sigma_fd:{sig_fd}')
print(f'5 - p<=2:{soma_fdp_p2*100}, p10:{p10*100}')