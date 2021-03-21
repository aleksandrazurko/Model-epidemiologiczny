import numpy as np
import matplotlib.pyplot as plt

x = np.zeros((80,80))

x[0][2] = 1
x[1][2] = 1
x[0][3] = 1
x[50][30] = 1
x[41][30] = 1
x[41][31] = 1
x[41][32] = 1
x[40][33] = 1

def gra_w_zycie(x):
    
    y = x.copy()
    X = int(len(x)-1)
    
    kumple = 0
    if x[0][1]:
        kumple += 1
    if x[1][0]:
        kumple += 1
    if x[1][1]:
        kumple += 1
    if not x[0][0]:
        if kumple == 3:
            y[0][0] == 1
        
    if x[0][0]:
        if kumple != 2 and kumple != 3:
            y[0][0] == 0
            
    kumple = 0
    if x[0][int(X-1)]:
        kumple += 1
    if x[1][X]:
        kumple += 1
    if x[1][int(X-1)]:
        kumple += 1
    if not x[0][X]:
        if kumple == 3:
            y[0][X] == 1
        
    if x[0][X]:
        if kumple != 2 and kumple != 3:
            y[0][X] == 0
    
    
    kumple = 0
    if x[X][1]:
        kumple += 1
    if x[int(X-1)][0]:
        kumple += 1
    if x[int(X-1)][1]:
        kumple += 1
    if not x[0][0]:
        if kumple == 3:
            y[X][0] == 1
        
    if x[0][0]:
        if kumple != 2 and kumple != 3:
            y[X][0] == 0
    
    
    kumple = 0
    if x[X][int(X-1)]:
        kumple += 1
    if x[int(X-1)][X]:
        kumple += 1
    if x[int(X-1)][int(X-1)]:
        kumple += 1
    if not x[X][X]:
        if kumple == 3:
            y[X][X] == 1
        
    if x[X][X]:
        if kumple != 2 and kumple != 3:
            y[X][X] == 0
            
    #WNETRZE
    for j in range(1,X):
        for i in range(1,X):
            kumple = 0
            if x[j-1][i-1]: kumple += 1
            if x[j-1][i]: kumple += 1
            if x[j-1][i+1]: kumple += 1
            if x[j][i-1]: kumple += 1
            if x[j][i+1]: kumple += 1
            if x[j+1][i-1]: kumple += 1
            if x[j+1][i]: kumple += 1
            if x[j+1][i+1]: kumple += 1
            if not x[i][j]:
                if kumple == 3:
                    y[i][j] == 1
            if x[i][j]:
                if kumple != 2 and kumple != 3:
                    y[i][j] == 0
        
    
    for i in range(1,X):
        kumple = 0
        kumple1 = 0
        kumple2 = 0
        kumple3 = 0
        if x[0][i-1]: kumple += 1
        if x[0][i+1]: kumple += 1
        if x[1][i-1]: kumple += 1
        if x[1][i]: kumple += 1
        if x[1][i+1]: kumple += 1
        if x[X][i-1]: kumple1 += 1
        if x[X][i+1]: kumple1 += 1
        if x[int(X-1)][i-1]: kumple1 += 1
        if x[int(X-1)][i]: kumple1 += 1
        if x[int(X-1)][i+1]: kumple1 += 1
        if x[i-1][0]: kumple2 += 1
        if x[i+1][0]: kumple2 += 1
        if x[i-1][1]: kumple2 += 1
        if x[i][1]: kumple2 += 1
        if x[i+1][1]: kumple2 += 1
        if x[i-1][X]: kumple3 += 1
        if x[i+1][X]: kumple3 += 1
        if x[i-1][int(X-1)]: kumple3 += 1
        if x[i][int(X-1)]: kumple3 += 1
        if x[i+1][int(X-1)]: kumple3 += 1
        if not x[0][i]:
            if kumple == 3:
                y[0][i] == 1
        if x[0][i]:
            if kumple != 2 and kumple != 3:
                y[0][i] == 0
        if not x[X][i]:
            if kumple1 == 3:
                y[X][i] == 1
        if x[X][i]:
            if kumple1 != 2 and kumple1 != 3:
                y[X][i] == 0
        if not x[i][0]:
            if kumple2 == 3:
                y[i][0] == 1
        if x[i][0]:
            if kumple2 != 2 and kumple2 != 3:
                y[i][0] == 0
        if not x[i][X]:
            if kumple3 == 3:
                y[i][X] == 1
        if x[i][X]:
            if kumple3 != 2 and kumple3 != 3:
                y[i][X] == 0                

            
    plt.figure(1)
    plt.imshow(x, cmap='Greys', interpolation='nearest')
    plt.figure(2)
    plt.imshow(y, cmap='Greys', interpolation='nearest')
    plt.show()

gra_w_zycie(x)

for i in range(1,3):
    print(i)