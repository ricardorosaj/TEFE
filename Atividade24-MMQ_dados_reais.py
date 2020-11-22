import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sigfig

df = pd.read_csv('dados_osciloscopio.txt', sep=' ')

si = 0.06 * np.ones(len(df)) #V

tensao = np.array(df['tensao'])
tempo = np.array(df['tempo'])

plt.plot(tempo, tensao, ls='', marker='.')
plt.title('Dados do Osciloscópio com f=2Hz')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.savefig('atv24-graf1.png')
# plt.show()
g1 = np.cos(4*np.pi*tempo)
g2 = np.sin(4*np.pi*tempo)
g = np.array((g1, g2))

D = np.zeros((2,1))
A = np.zeros((2,1))
M = np.zeros((2,2))

for i in range(2):
    D[i] = np.sum((g[i]*tensao)/(si**2))
    for j in range(2):
        M[i][j] = np.sum((g[i]*g[j])/(si**2))
#item a
Va = np.linalg.inv(M)
A = np.matmul(Va,D)
a = A[0][0]
b = A[1][0]
sa = np.sqrt(Va[0][0])
sb = np.sqrt(Va[1][1])
print(f'a) Parametros: a={a} +- {sa}, b={b} +- {sb}')
#item b
cov = float(Va[0][1])
rho = float(cov/np.sqrt(Va[0][0]*Va[1][1]))
print(f'b) cov = {sigfig.round(cov, sigfigs=3)}, rho = {rho}')#{sigfig.round(rho, decimals=3)}')
#item c
A = str(np.sqrt(a**2+b**2))
sa = str(np.sqrt((a**2 * sa**2 + b**2 * sb**2)/(a**2 + b**2) + 2*a*b/(a**2+b**2)*cov))
print(f'c) Amplitude: {sigfig.round(A, uncertainty=sa)}') 
#item d
F = a*g1 + b*g2
plt.plot(tempo, F, color='r')
plt.scatter(tempo, tensao, s=5)
plt.title('Ajuste realizado nos dados')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.savefig('atv24-d1.png')
plt.show()

plt.scatter(tempo,tensao-F, s=5)
plt.title('Resíduos do ajuste')
plt.xlabel('Tempo (s)')
plt.ylabel('Tensão (V)')
plt.savefig('atv24-d2.png')
plt.show()

#item e
chi2 = float(np.sum(((tensao-F)/si)**2))
print(f'e) chi2: {sigfig.round(chi2, decimals=1)}, NGL: {len(df)-2}')