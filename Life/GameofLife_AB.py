# -*- coding: utf-8 -*-
"""
Created on Tue Mar 16 22:17:52 2021

@author: HP
"""
import numpy as np


przestrzen=np.zeros((6,6))
#zywe komorki
index_1=(1,1)
index_2=(2,1)
index_3=(3,1)
index_4=(0,4)

przestrzen[index_1]=1
przestrzen[index_2]=1
przestrzen[index_3]=1
przestrzen[index_4]=1

print('Macierz początkowa:')
print(przestrzen)
#print(index_2[1])

#nowa generacja
n_przestrzen=np.zeros((6,6))

for x in range(0,len(n_przestrzen)):
    for y in range(0,len(n_przestrzen)):
        oznaki_zycia=0
        for k in range(-1,2):
            for i in range(-1,2):
                if x+k>len(n_przestrzen)-1 or y+i>len(n_przestrzen)-1:
                    pass                   
                else:
                    if k==0 and i==0:
                        pass
                    else:
                        oznaki_zycia+=przestrzen[x+k,y+i]
        if oznaki_zycia==2 and przestrzen[x,y]!=0:
            n_przestrzen[x,y]=1
        if oznaki_zycia==3:
            n_przestrzen[x,y]=1
            
            
print('Nowa generacja:')           
print(n_przestrzen)

        
