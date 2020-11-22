import numpy as np
import sigfig
import matplotlib.pyplot as plt
#D=MA com A=[a1,a2]

t = np.array([1,2,3,4,5])
h = np.array([1.7, 3.0, 4.2, 4.8, 5.4])
sh = np.array(5*[0.2])

g = np.array((5*[1],[1,2,3,4,5]))

D = np.zeros((2,1))
A = np.zeros((2,1))
M = np.zeros((2,2))

for i in range(2):
    D[i] = np.sum((g[i]*h)/(sh**2))
    for j in range(2):
        M[i][j] = np.sum((g[i]*g[j])/(sh**2))

#item a
Va = np.linalg.inv(M)
A = np.matmul(Va,D)
a = A[0][0]
b = A[1][0]
sa = np.sqrt(Va[0][0])
sb = np.sqrt(Va[1][1])
print(f'a) Parametros: a={a} +- {sa}, b={b} +- {sb}\nMatriz de covariancias:\n{Va}')
#item b
cov = float(Va[0][1])
rho = float(cov/np.sqrt(Va[0][0]*Va[1][1]))
print(f'b) cov: {sigfig.round(cov, sigfigs=3)}, rho: {sigfig.round(rho, sigfigs=3)}')
#item c
F = a + b*t
chi2 = float(np.sum(((h-F)/sh)**2))
print(f'c) chi2: {sigfig.round(chi2, decimals=1)}, NGL: 3')
#item D
t1 = 1.5
t2 = 6.0
h1 = a + b*t1
sh1 = np.sqrt(sa**2 + (t1*sb)**2 + 2*t1*cov)
h2 = a + b*t2
sh2 = np.sqrt(sa**2 + (t2*sb)**2 + 2*t2*cov)
print(f'''d) Pos em t=1.5s: {h1} +- {sh1}\n
Pos em t=6s: {h2} +- {sh2}''')

#item e
g = np.array((5*[1], g[1]-3))
for i in range(2):
    D[i] = np.sum((g[i]*h)/(sh**2))
    for j in range(2):
        M[i][j] = np.sum((g[i]*g[j])/(sh**2))
Va = np.linalg.inv(M)
A = np.matmul(Va,D)
a = A[0][0]
b = A[1][0]
sa = np.sqrt(Va[0][0])
sb = np.sqrt(Va[1][1])
print(f'e) Parametros: ã={a} +- {sa}, b~={b} +- {sb}\nMatriz de covariancias:\n{Va}')
cov = float(Va[0][1])
rho = float(cov/np.sqrt(Va[0][0]*Va[1][1]))
print(f'cov: {sigfig.round(cov, sigfigs=3)}, rho: {sigfig.round(rho, sigfigs=3)}')
F = a + b*(t-3)
chi2 = float(np.sum(((h-F)/sh)**2))
print(f'chi2: {sigfig.round(chi2, decimals=1)}, NGL: 3')
t1 = 1.5
t2 = 6.0
h1 = a + b*(t1-3)
sh1 = np.sqrt(sa**2 + ((t1-3)*sb)**2 + 2*(t1-3)*cov)
h2 = a + b*(t2-3)
sh2 = np.sqrt(sa**2 + ((t2-3)*sb)**2 + 2*(t2-3)*cov)
print(f'''Pos em t=1.5s: {h1} +- {sh1}\n
Pos em t=6s: {h2} +- {sh2}''')