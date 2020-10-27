import numpy as np
import sigfig
import matplotlib.pyplot as plt

x0=110
y0=100
sc=4
sl=3
def gera_num_1(N):
    lista_x = np.zeros(N)
    lista_y = np.zeros(N)
    for i in range(N):
        ec = sc*np.random.normal(0,1)
        x = x0 + sl*np.random.normal(0,1) + ec
        y = y0 + sl*np.random.normal(0,1) + ec
        lista_x[i] = x
        lista_y[i] = y
    sx = np.std(lista_x)
    sy = np.std(lista_y)
    n=0
    soma_vxy = 0
    for i in range(N):
        soma_vxy += (lista_x[i]-x0)*(lista_y[i]-y0)
        if (lista_x[i]-x0>0 and lista_y[i]-y0>0) or (lista_x[i]-x0<0 and lista_y[i]-y0<0):
            n+=1
    f = n/N
    inc_n = sigfig.round(float(np.sqrt(N*f*(1-f))), sigfigs=2)
    inc_f = sigfig.round(inc_n/N, sigfigs=2)

    v_xy = soma_vxy/(N-1)
    R = v_xy/(sx*sy)
    inc_v_xy = sigfig.round(float(sx*sy*np.sqrt((1+R**2)/(N-1))), sigfigs=2)
    inc_R = sigfig.round(float((1-R**2)/np.sqrt(N-1)), sigfigs=2)

    w = lista_x + lista_y
    std_w = np.std(w)
    inc_std_w = sigfig.round(float(std_w/np.sqrt(2*(N-1))), sigfigs=2)
    z = lista_x - lista_y
    std_z = np.std(z)
    inc_std_z = sigfig.round(float(std_z/np.sqrt(2*(N-1))), sigfigs=2)

    std_w_e_z_sem_cov = np.sqrt(sx**2 + sy**2)

    print(f'a: f = {f} +- {inc_f}')
    print(f'b: V_xy = {v_xy} +- {inc_v_xy}, R = {R} +- {inc_R}')
    print(f'c: std_w = {std_w} +- {inc_std_w}')
    print(f'd: std_z = {std_z} +- {inc_std_z}')
    print(f'e: propag inc = {std_w_e_z_sem_cov}')
    return [lista_x, lista_y]

def plota(func):
    x = func[0]
    y = func[1]
    plt.scatter(x,y,s=3)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Dispersão de x e y')
    plt.show()

d0 = 200
ss = 4
sa = 3
def gera_num_2(N,M):
    d = np.zeros((M,N))
    for i in range(M):
        for j in range(N):
            di = d0 + ss*np.random.normal(0,1) + sa*np.random.normal(0,1)
            d[i][j] = di
    Med = np.mean(d, axis=1)
    sdm = np.std(Med)
    inc_sdm = sdm/(np.sqrt(2*(M-1)))
    print(f'2: sdm = {sdm} +- {inc_sdm}')

func1 = gera_num_1(1000)
plota(func1)
func2 = gera_num_2(25,10000)