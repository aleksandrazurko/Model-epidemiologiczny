# -*- coding: utf-8 -*-


import numpy as np


przestrzen=np.zeros((10,10))

#położenie mrówki
ant=[5,6]
ant_head=[4,6]
przestrzen[tuple(ant)]=1
print(przestrzen)

ilosc_ruchow=10

#[rzedy, kolumnty]



while ilosc_ruchow:
    if przestrzen[tuple(ant)]==1:
        przestrzen[tuple(ant)]=0
        if ant[0]-ant_head[0]==0 and ant[1]-ant_head[1]==1 :
            ant[1]=ant[1]+1
            ant_head=ant
            ant_head=ant_head[1]+1
            ilosc_ruchow=ilosc_ruchow-1
        elif ant[0]-ant_head[0]==0 and ant[1]-ant_head[1]==-1 :
            ant[1]=ant[1]-1
            ant_head=ant
            ant_head=ant_head[1]-1
            ilosc_ruchow=ilosc_ruchow-1   
        elif ant[0]-ant_head[0]==1 and ant[1]-ant_head[1]==0 :
            ant[0]=ant[0]-1
            ant_head=ant
            ant_head=ant_head[0]+1
            ilosc_ruchow=ilosc_ruchow-1
        else: #ant[0]-ant_head[0]==-1 and ant[1]-ant_head[1]==0:
            ant[0]=ant[0]+1
            ant_head=ant
            ant_head=ant_head[0]+1
            ilosc_ruchow=ilosc_ruchow-1
    else:
        przestrzen[tuple(ant)]=1
        if ant[0]-ant_head[0]==0 and ant[1]-ant_head[1]==1 :
            ant[1]=ant[1]-1
            ant_head=ant
            ant_head=ant_head[1]-1
            ilosc_ruchow=ilosc_ruchow-1
        elif ant[0]-ant_head[0]==0 and ant[1]-ant_head[1]==-1 :
            ant[1]=ant[1]+1
            ant_head=ant
            ant_head=ant_head[1]+1
            ilosc_ruchow=ilosc_ruchow-1   
        elif ant[0]-ant_head[0]==1 and ant[1]-ant_head[1]==0 :
            ant[0]=ant[0]+1
            ant_head=ant
            ant_head=ant_head[0]+1
            ilosc_ruchow=ilosc_ruchow-1
        else: #ant[0]-ant_head[0]==-1 and ant[1]-ant_head[1]==0 :
            ant[0]=ant[0]-1
            ant_head=ant
            ant_head=ant_head[0]-1
            ilosc_ruchow=ilosc_ruchow-1
                
                
print('po przejsciu')       
print(przestrzen)