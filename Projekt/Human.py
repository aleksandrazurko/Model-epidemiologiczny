from Graph import *
from Space import *
from Vertex import *
import random
import numpy as np
import matplotlib.pyplot as plt

class Human():
    #konstruktor
    def __init__(self,position, status, mask): 
        self.__position = position
        self.__status = status
        self.__mask = mask

    #destruktor
    def __del__(self):
        return()

    def ChangeStatus(self, new_status):
        self.__status = new_status

    def GetStatus(self):
        return(self.__status)

    #wykonanie kroku
    def Step(self, parent):
        _,paths, probability = parent.GetBack(self.__position)
        los = random.random()
        suma = 0
        ind = 0
        for p in probability:
            if (p/100 + suma) > los:
                break
            else:
                suma += p/100
                ind += 1
        if parent.Available(paths[int(ind)],self.__position) == True:
            self.__position = paths[int(ind)]
        return(self.__position)

#raport danych np. ile osob wyszło
''' def Report(self):
print(self.counter_in)
print(self.counter_out)'''
