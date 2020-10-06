import numpy as np

#1)
def monte_carlo_pi(N): #N=1000
    n = 0
    for i in range(N):
        u1 = np.random.uniform()
        u2 = np.random.uniform()
        if u1**2 + u2**2 <= 1:
            n+=1
    p = n/N
    sigma_n = np.sqrt(N*p*(1-p))
    x = 4*n/N
    sigma_x = 4*sigma_n/N
    print(f'1) n: {n}, sigma_n: {sigma_n}, pi:{x} +- {sigma_x}')

monte_carlo_pi(1000)    

#2)
def monte_carlo_pi_3d(N): #N=500
    n = 0
    for i in range(N):
        u1 = np.random.uniform()
        u2 = np.random.uniform()
        u3 = np.random.uniform()
        if u1**2 + u2**2 + u3**2 <= 1:
            n+=1
    p = n/N
    sigma_n = np.sqrt(N*p*(1-p))
    x = 6*n/N
    sigma_x = 6*sigma_n/N
    print(f'2) n: {n}, sigma_n: {sigma_n}, pi:{x} +- {sigma_x}')

monte_carlo_pi_3d(500)    