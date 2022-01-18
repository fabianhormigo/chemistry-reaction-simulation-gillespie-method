# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 04:31:42 2022

@author: fabia
"""


""

_author__ = "Fabian Hormigo Pereila"
__copyright__ = "Copyright (C) 2021 Fabian Hormigo Pereila"
__license__ = "Public Domain"
__version__ = "1.0"
import numpy as np 
from matplotlib import pyplot as plt
from reactionfourparams import reactionfour 


#generador apertura y cierre estudio de los datos

tracks=1

    #number of total cells

    #number of initial open cells for each truck(vectorized fun)
n_1=310*np.ones(tracks)
n_2=62*np.ones(tracks)
n_3=0*np.ones(tracks)
n_4=0*np.ones(tracks)



acumuladortime=np.zeros([tracks,800])

acumuladorn1=np.zeros([tracks,800])
acumuladorn2=np.zeros([tracks,800])
acumuladorn3=np.zeros([tracks,800])
acumuladorn4=np.zeros([tracks,800])

acumuladormedio1=[]
acumuladormedio4=[]
acumuladorstd1=[]
acumuladorstd4=[]
acumuladormedio2=[]
acumuladormedio3=[]

for k in range(800):
    
    [deltan_1,deltan_2,deltan_3,deltan_4,tau]=reactionfour(n_1,n_2,n_3,n_4)
    
    acumuladorn1[:,k]=n_1+deltan_1
    acumuladorn2[:,k]=n_2+deltan_2
    acumuladorn3[:,k]=n_3+deltan_3
    acumuladorn4[:,k]=n_4+deltan_4
    
    acumuladortime[:,k]=tau
    n_1=n_1+deltan_1
    n_2=n_2+deltan_2
    n_3=n_2+deltan_3
    n_4=n_2+deltan_4
    
    valoremedion_1=np.median(n_1)
    valoremedion_2=np.median(n_2)
    valoremedion_3=np.median(n_3)
    
    valoremedion_4=np.median(n_4)
    
    std1=np.std(n_1)
    std4=np.std(n_4)
    
    acumuladorstd1=np.append(acumuladorstd1,std1)
    acumuladorstd4=np.append(acumuladorstd4,std4)
    
    acumuladormedio1=np.append(acumuladormedio1,valoremedion_1)
    acumuladormedio2=np.append(acumuladormedio2,valoremedion_2)
    acumuladormedio3=np.append(acumuladormedio3,valoremedion_3)
    acumuladormedio4=np.append(acumuladormedio4,valoremedion_4)
   
    
 
    
    
    

#ploteo histograma y valores medios
n1=np.array(acumuladorn1)
n2=np.array(acumuladorn2)
n3=np.array(acumuladorn3)
n4=np.array(acumuladorn4)



n1_medio=acumuladormedio1
n2_medio=acumuladormedio2
n3_medio=acumuladormedio3

n4_medio=acumuladormedio4

#plot valor medio y valor medio cuadrado t


plt.figure(4)
plt.plot(n1_medio)

plt.ylabel('Número de partículas 4')
plt.xlabel('t')










