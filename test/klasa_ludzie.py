# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
import numpy as np

class czlowiek():
    def __init__(self, maska, odpornosc, zarazenie):
        self.__pozycja = [0,0]
        self.__szlak = []
        self.__maska = maska
        self.__odpornosc = odpornosc
        self.__zarazenie = zarazenie
    
    def krok(self, liczba):
        for i in range(liczba):
            try:
                random.seed(10)
                kierunekx = random.choice([0,0,1,1,1,1,-1,-1,-1,-1])
                kieruneky = random.choice([0,0,0,0,1,1,1,-1,-1,-1])
                self.__szlak.append(self.__pozycja)
                self.__pozycja[0] += kierunekx
                self.__pozycja[1] += kieruneky
            except:
                czlowiek.krok(self)
    
    def pozycja(self):
        return self.__pozycja
    
    def szlak(self):
        return self.__szlak
    
    def atrybuty(self):
        return (self.__maska, self.__odpornosc, self.__zarazenie)

zosia = czlowiek(True, False, False)
zosia.krok(5)
#print(zosia.pozycja())
#print(zosia.atrybuty())
kasia = czlowiek(True, False, True)
kasia.krok(4)
#print(kasia.pozycja())
#print(kasia.atrybuty())

czlowiek_pozycja = [zosia.pozycja(), kasia.pozycja()]
czlowiek_atrybuty = [zosia.atrybuty(), kasia.atrybuty()]

#print(type(czlowiek_pozycja[0]))
class sasiedzi():
    def __init__(self, czlowiek_atrybuty, czlowiek_pozycja):
        self.__czlowiek_atrybuty = czlowiek_atrybuty
        self.__czlowiek_pozycja = czlowiek_pozycja
        self.__sasiedzi = []

    def sasiedzi(self):
        for x, y in czlowiek_pozycja:
            if [x, y+1] in self.__czlowiek_pozycja and [[x, y+1], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x, y+1]])
            elif [x-1, y] in self.__czlowiek_pozycja and [[x-1, y], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x-1, y]])
            elif [x, y-1] in self.__czlowiek_pozycja and [[x, y-1], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x, y-1]])
            elif [x-1, y+1] in self.__czlowiek_pozycja and [[x-1, y+1], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x-1, y+1]])
            elif [x-1, y-1] in self.__czlowiek_pozycja and [[x-1, y-1], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x-1, y-1]])
            elif [x+1, y] in self.__czlowiek_pozycja and [[x+1, y], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x+1, y]])
            elif [x+1, y-1] in self.__czlowiek_pozycja and [[x+1, y-1], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x+1, y-1]])
            elif [x+1, y+1] in self.__czlowiek_pozycja and [[x+1, y+1], [x, y]] not in self.__sasiedzi:
                self.__sasiedzi.append([[x, y], [x+1, y+1]])
        return self.__sasiedzi
                
test = sasiedzi(czlowiek_atrybuty, czlowiek_pozycja)
#print(len(czlowiek_pozycja))
print(test.sasiedzi())


class zarazanie():
    def __init__(self, sasiedzi, czlowiek_atrybuty, czlowiek_pozycja):
        self.__czlowiek_atrybuty = czlowiek_atrybuty
        self.__sasiedzi = sasiedzi
        self.__czlowiek_pozycja = czlowiek_pozycja
        self.__atrybuty_sasiadow = []
    
    def zarazanie(self):
        for czlowiek1, czlowiek2 in self.__sasiedzi:
            ind1 = self.__czlowiek_pozycja.index(czlowiek1)
            ind2 = self.__czlowiek_pozycja.index(czlowiek2)
            self.__atrybuty_sasiadow.append([self.__czlowiek_atrybuty[ind1], self.__czlowiek_atrybuty[ind2]])
        #for para in self.__atrybuty_sasiadow:
        return self.__atrybuty_sasiadow

print(np.shape(test.sasiedzi()))
z = zarazanie(test.sasiedzi(), czlowiek_atrybuty, czlowiek_pozycja)
#print(z.zarazanie())        


print(np.zeros([2,2,2]))





