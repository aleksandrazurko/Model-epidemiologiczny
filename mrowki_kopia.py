import numpy as np

macierz = np.array([[1, 1, 0, 1], [0, 1, 1, 0], [0, 1, 1, 0], [1, 0, 0, 1]])


def pierwszy_krok(macierz):
    rzad, kolumna = np.shape(macierz)
    nowa_macierz = np.zeros([rzad, kolumna])
    for i in range(rzad):
        for j in range(kolumna):
            if i == 0 and j == 0:
                sasiedzi = macierz[i, j+1] + macierz[i+1, j] + macierz[i+1, j+1]
            elif i == 0 and j == kolumna-1:
                sasiedzi = macierz[i, j-1] + macierz[i+1, j-1] + macierz[i+1, j]
            elif i == 0:
                sasiedzi = macierz[i, j-1] + macierz[i, j+1] + macierz[i+1, j-1] + macierz[i+1, j] + macierz[i+1, j+1]
            elif i == rzad-1 and j == 0:
                sasiedzi = macierz[i-1, j] + macierz[i-1, j+1] + macierz[i, j+1]
            elif j == 0:
                sasiedzi = macierz[i-1, j] + macierz[i-1, j+1] + macierz[i, j+1] + macierz[i+1, j] + macierz[i+1, j+1]
            elif i == rzad-1 and j == kolumna-1:
                sasiedzi = macierz[i-1, j] + macierz[i-1, j-1] + macierz[i, j-1]
            elif i == rzad-1:
                sasiedzi = macierz[i-1, j-1] + macierz[i-1, j] + macierz[i-1, j+1] + macierz[i, j-1] + macierz[i, j+1]
            elif j == kolumna-1:
                sasiedzi = macierz[i-1, j-1] + macierz[i-1, j] + macierz[i, j-1] + macierz[i+1, j-1] + macierz[i+1, j]
            else:
                sasiedzi = macierz[i,j-1] + macierz[i,j+1] + macierz[i-1, j-1] + macierz[i-1, j] + macierz[i-1, j+1] + macierz[i+1, j-1] + macierz[i+1, j] + macierz[i+1, j+1]
            if macierz[i, j] == 0:
                if sasiedzi == 3:
                    nowa_macierz[i, j] = 1
            elif macierz[i, j] == 1:
                if sasiedzi == 2 or sasiedzi == 3:
                    nowa_macierz[i, j] = 1
    return nowa_macierz



def nastepne_kroki(macierz, liczba_krokow):
    for i in range(liczba_krokow):
        macierz = pierwszy_krok(macierz)
    return macierz

print(nastepne_kroki(macierz, 11))