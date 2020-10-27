import numpy as np
import matplotlib.pyplot as plt
import sigfig

a0 = 30
b0 = 20
sig_a = 2
sig_b = 2
N=500

def gera_num(N, rho):
    list_a = np.zeros(N)
    list_b = np.zeros(N)
    for i in range(N):
        r1 = np.random.normal(0,1)
        r2 = np.random.normal(0,1)
        a = a0 + sig_a*r1
        b = b0 + sig_b*(rho*r1+r2*np.sqrt(1-rho**2))
        list_a[i] = a
        list_b[i] = b
    
    sa = np.std(list_a)
    sb = np.std(list_b)
    n=0
    soma_vab = 0
    for i in range(N):
        soma_vab += (list_a[i]-a0)*(list_b[i]-b0)
        if (list_a[i]-a0>0 and list_b[i]-b0>0) or (list_a[i]-a0<0 and list_b[i]-b0<0):
            n+=1

    f = n/N
    inc_n = sigfig.round(float(np.sqrt(N*f*(1-f))), sigfigs=2)
    inc_f = sigfig.round(inc_n/N, sigfigs=2)

    v_ab = soma_vab/(N-1)
    R = v_ab/(sa*sb)
    inc_v_ab = sigfig.round(float(sa*sb*np.sqrt((1+R**2)/(N-1))), sigfigs=2)
    inc_R = sigfig.round(float((1-R**2)/np.sqrt(N-1)), sigfigs=2)

    w = list_a + list_b
    std_w = np.std(w)
    inc_std_w = sigfig.round(float(std_w/np.sqrt(2*(N-1))), sigfigs=2)
    z = list_a - list_b
    std_z = np.std(z)
    inc_std_z = sigfig.round(float(std_z/np.sqrt(2*(N-1))), sigfigs=2)

    print(f'Caso com rho={rho}')
    print(f'a1: n = {n} +- {inc_n}')
    print(f'a2: f = {f} +- {inc_f}')
    print(f'a3: V_ab = {v_ab} +- {inc_v_ab}, R = {R} +- {inc_R}')
    print(f'a4: std_w = {std_w} +- {inc_std_w}')
    print(f'a5: std_z = {std_z} +- {inc_std_z}\n')
    return [list_a, list_b]

def plota(func,rho):
    a = func[0]
    b = func[1]
    plt.scatter(a,b,s=3)
    plt.xlabel('a')
    plt.ylabel('b')
    plt.title(f'rho = {rho}')
    plt.show()

func1 = gera_num(N, 0.75)
plota(func1, 0.75)
func2 = gera_num(N, -0.75)
plota(func2, -0.75)

rhos = [0, -0.25, 0.5, -0.9, 0.95]
for rho in rhos:
    func = gera_num(N, rho)
    plota(func, rho)