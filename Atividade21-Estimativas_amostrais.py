import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sigfig import round as r

def gera(N,M):
    x = np.zeros((M,N))
    V = np.zeros(M)
    s = np.zeros(M)
    for i in range(M):
        x[i] = np.random.randn(N)
    V = np.var(x,axis=1, ddof=1)
    s = np.std(x,axis=1, ddof=1)

    #if N==100 or N==5 or N==2:
        # plt.hist(V, bins=10)
        # plt.title(f'Variância - N={N}')
        # plt.show()

        # plt.hist(s, bins=10)
        # plt.title(f'Desv. Pad. Amostral - N={N}')
        # plt.show() 
    return [s,V]

ns = [100, 50, 10, 5, 4, 3, 2]

dict_entrega = {'N=100':0, 'N=50':0, 'N=10':0, 'N=5':0, 'N=4':0, 'N=3':0, 'N=2':0}
index = ['sm', 'Vm', '# s <= s0', '# V <= V0']
M=10000
for N in ns:
    conta_s = 0
    conta_V = 0
    func = gera(N,M)
    sm = np.mean(func[0])
    inc_sm = np.std(func[0], ddof=1)/np.sqrt(len(func[0]))
    Vm = np.mean(func[1])
    inc_Vm = np.std(func[1], ddof=1)/np.sqrt(len(func[1]))
    for i in range(M):
        if func[0][i] <= 1:
            conta_s+=1
        if func[1][i] <= 1:
            conta_V+=1
    fs = conta_s/M
    fv = conta_V/M
    inc_conta_s = np.sqrt(M*fs*(1-fs))   
    inc_conta_V = np.sqrt(M*fv*(1-fv))     
    dict_entrega[f'N={N}']=[r(f'{sm}', uncertainty=f'{inc_sm}'),
        r(f'{Vm}',uncertainty=f'{inc_Vm}'), r(f'{conta_s}', uncertainty=f'{inc_conta_s}'),
        r(f'{conta_V}', uncertainty=f'{inc_conta_V}')]
data = pd.DataFrame(dict_entrega, index=index)
data.to_csv('atividade21.csv')