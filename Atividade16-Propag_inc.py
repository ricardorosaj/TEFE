import numpy as np
import random

x0 = 15
y0 = 40
sig_x = 2
sig_y = 3
M=10000

def calcula_w(nx, ny):
    w=np.zeros(M)
    x=np.zeros(nx)
    y=np.zeros(ny)
    for i in range(M):
        for j in range(nx):
            x[j] = random.gauss(x0, sig_x) 
        xm = np.mean(x)    
        for j in range(ny):
            y[j] = random.gauss(y0, sig_y)
        ym = np.mean(y)
        w[i] = xm*ym
    print(f'Caso nx={nx} e ny:{ny}: wm:{np.mean(w)}, sw:{np.std(w)}')    

#a
calcula_w(1,1)
#b1
calcula_w(2,1)
#b2
calcula_w(1,2)
#c
nx=1
while nx <= 10:
    ny=11-nx
    calcula_w(nx,ny)
    nx+=1