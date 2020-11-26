import numpy as np
import sigfig
import matplotlib.pyplot as plt

a0 = 20 #cm
b0 = 3 #cm/s  

ti = np.arange(0,11,1) #s
sl = 0.5*np.ones(11) #cm

g1 = np.ones(11)
g2 = np.arange(0,11,1)
g = np.array((g1, g2))

D = np.zeros((2,1))
A = np.zeros((2,1))
M = np.zeros((2,2))

for i in range(2):
    for j in range(2):
        M[i][j] = np.sum((g[i]*g[j])/(sl**2))
#item a
Va = np.linalg.inv(M)
sa = np.sqrt(Va[0][0])
sb = np.sqrt(Va[1][1])
cov = float(Va[0][1])
rho = float(cov/np.sqrt(Va[0][0]*Va[1][1]))
print(f'a) Inc Parametros: sa = {sa} cm, sb = {sb} cm, rho = {sigfig.round(rho,decimals=3)}\n{Va}')
#item b
a = np.random.normal(a0,sa,11)
b = np.random.normal(b0,sb,11)
yi = a*g1+b*g2
# plt.plot(ti, F0)
# plt.scatter(ti,yi)
# plt.show()
for i in range(2):
    D[i] = np.sum((g[i]*yi)/(sl**2))
A = np.matmul(Va,D)
a = A[0][0]
b = A[1][0]   
F = a + b*ti
chi2 = float(np.sum(((yi-F)/sl)**2))
print(f'b) a = {a} cm, b = {b} cm, chi2 = {chi2}, NGL = {len(yi)-len(A)}')
#item c
Nrep=10000
chi2_list = np.zeros(Nrep)
a_list = np.zeros(Nrep)
b_list = np.zeros(Nrep)
for i in range(Nrep):
    ai = np.random.normal(a0,sa,11)
    bi = np.random.normal(b0,sb,11)
    yi = ai*g1+bi*g2
    for j in range(2):
        D[j] = np.sum((g[j]*yi)/(sl**2))
    A = np.matmul(Va,D)
    a = A[0][0]
    b = A[1][0]   
    F = a + b*ti
    chi2 = float(np.sum(((yi-F)/sl)**2))
    chi2_list[i] = chi2
    a_list[i] = a
    b_list[i] = b
#item c1    
plt.hist(a_list)
plt.title('Frequência para parâmetro a')
plt.xlabel('Valores de a (cm)')
plt.savefig('atv25_hist_c1.png')
plt.show()

s_a = np.std(a_list)
inc_s_a = s_a/np.sqrt(2*(Nrep-1))
print(f'c1) desv pad a = {s_a} +- {inc_s_a}')
#item c2
plt.hist(b_list)
plt.title("Frequência para parâmetro b")
plt.xlabel('Valores de b (cm/s)')
plt.savefig('atv25_hist_c2.png')
plt.show()
s_b = np.std(b_list)
inc_s_b = s_b/np.sqrt(2*(Nrep-1))
print(f'c2) desv pad b = {s_b} +- {inc_s_b}')
#item c3
plt.scatter(a_list, b_list, s=4)
plt.title("Dispersão de a e b")
plt.xlabel('a (cm)')
plt.ylabel('b (cm/s)')
plt.savefig('atv25_scat_c3.png')
plt.show()
cov_amostral = np.mean((a_list - np.mean(a_list))*(b_list - np.mean(b_list)))
rho_amostral = cov_amostral/(s_a*s_b)
inc_rho_amostral = (1-rho_amostral**2)/np.sqrt(Nrep-1)
print(f'c3) correlação = {rho_amostral} +- {inc_rho_amostral}')
#item c4
plt.hist(chi2_list)
plt.title("Frequência para chi2")
plt.xlabel('Valores de chi2')
plt.savefig('atv25_hist_c4.png')
plt.show()
chi2_mean = np.mean(chi2_list)
inc_chi2_mean = np.std(chi2_list)/np.sqrt(Nrep)
print(f'c4) chi2 medio = {chi2_mean} +- {inc_chi2_mean}, NGL = 9')