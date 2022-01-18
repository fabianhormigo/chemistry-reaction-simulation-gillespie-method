# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 03:52:23 2022

@author: fabia
"""

__author__ = "Fabian Hormigo Pereila"
__copyright__ = "Copyright (C) 2021 Fabian Hormigo Pereila"
__license__ = "Public Domain"
__version__ = "1.0"
def reactionfour(n_1,n_2,n_3,n_4):
    import numpy as np 
    a_1=(1/602.3)*n_1*n_2
    a_2=a_1+0.0001*n_3
    a_3=a_2+0.1*n_3
    
    
    r1=np.random.uniform(0,1,len(n_1))
    r2=a_3*np.random.uniform(0,1,len(n_1))
    
    
    tau=np.log(1/r1)/a_3
    
    
    #Vector a llenar o delta de componentes
    va=[]
    vb=[]
    vc=[]
    vd=[]
    
    for k in range(len(n_1)):
        a_1k=a_1[k]
        a_2k=a_2[k]
        a_3k=a_3[k]
        r2k=r2[k]
        
        if a_1k>r2k:
           a=-1
           b=-1
           c=1
           d=0
           va=np.append(va,a)
           vb=np.append(vb,b)
           vc=np.append(vc,c)
           vd=np.append(vd,d)
            
        elif a_2k>r2k:
           a=1
           b=1
           c=-1
           d=0
           va=np.append(va,a)
           vb=np.append(vb,b)
           vc=np.append(vc,c)
           vd=np.append(vd,d)
        else:
           a=0
           b=1
           c=-1
           d=1
           va=np.append(va,a)
           vb=np.append(vb,b)
           vc=np.append(vc,c)
           vd=np.append(vd,d)
    
    
    return [va,vb,vc,vd,tau] 