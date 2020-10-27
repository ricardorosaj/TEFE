import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

df = pd.read_excel('new_leagues_data.xlsx', sheet_name='JPN')

def sig(N, p): return np.sqrt(N*p*(1-p))

def binomial(n, p): return (factorial(10)/(factorial(n)*factorial(10-n)))*(p**10)*((1-p)**(10-n))

def poisson(a, n): return (a**n/factorial(n))*np.exp(-a)

def count(n, gol):
    conta_gol = 0
    for i in range(len(df)):
        if df[gol][i] == n:
            conta_gol+=1
    inc_conta = np.sqrt(conta_gol)
    if conta_gol==0:
        inc_conta=1        
    freq = conta_gol/len(df)
    inc_freq = inc_conta/len(df)
    return [conta,inc_conta,freq,inc_freq]        

#1-
N = len(df)
print("N = ", N)

hg_avg = np.average(df["HG"])
std_hg = np.std(df["HG"], ddof = 1)
sigma_hg = std_hg/np.sqrt(N)

print('media de gols do mandante=', hg_avg)
print('desv pad da média =', sigma_hg)
print('desvio padrao amostral=', std_hg)

ha_avg = np.average(df["AG"])
std_ha =np.std(df["AG"], ddof = 1)
sigma_ha = std_ha/np.sqrt(N)

print()


print('media de gols do visitante=', ha_avg)
print('desv pad da média =', sigma_ha)
print('desvio padrao amostral=', std_ha)


def P(a,n):
    return ((a**n)*np.exp(-a))/np.math.factorial(n)

print('TABELA MANDANTE')
(n, bins, patches) = plt.hist(df["HG"], bins = 7)
for i in range(len(n)):
    sigma_n = np.sqrt(n[i]*(1-n[i]/N))
    print("n{} = {} # {:.3}".format(i,n[i],sigma_n),'|f=', n[i]/N, '#', sigma_n/N, '|', P(hg_avg,i))
plt.plot()
print() 

print('TABELA VISITANTE')
(n, bins, patches) = plt.hist(df["AG"], bins = 7)
for i in range(len(n)):
    sigma_n = np.sqrt(n[i]*(1-n[i]/N))
    print("n{} = {} # {:.3}".format(i,n[i],sigma_n),'|f=', n[i]/N, '#', sigma_n/N, '|', P(ha_avg,i))
plt.plot()
print()



T = np.zeros(N)
for i in range(N):
    T[i] = df['HG'][i] + df['AG'][i] 

media_T = np.mean(T)
sigma_T = np.std(T, ddof=1)
sigma_media_T = sigma_T/np.sqrt(N)


print('media de numero total de gols=', media_T, '#', sigma_media_T)
print('desvio amostral=', sigma_T)


print(np.sqrt(media_T))