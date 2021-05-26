from Graph import *
from Space import *
from Vertex import *
import random
import numpy as np
import matplotlib.pyplot as plt
import pygame as pg

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

    def GetPosition(self):
        return(self.__position)

    def GetStatus(self):
        return(self.__status)

    def GetMask(self):
        return(self.__mask)

    def Show(self,screen):
        scale = 50
        if self.__status == 'I':
            pg.draw.circle(screen, (255,0,0), (self.__position[0]*scale,self.__position[1]*scale), 10)
        else:
            pg.draw.circle(screen, (100, 240, 50), (self.__position[0]*scale,self.__position[1]*scale), 10)

    def Hide(self,screen, max_humans):
        scale = 50
        for i in range(max_humans):
            pg.draw.circle(screen, (0, 0, 0), (self.__position[0]*scale, self.__position[1]*scale + i*5), 5)


    #wykonanie kroku
    def Step(self, parent1,parent2, max_humans):
        _,paths, probability = parent1.GetBack(self.__position)
        los = random.random()
        suma = 0
        ind = 0
        for p in probability:
            if (p/100 + suma) > los:
                break
            else:
                suma += p/100
                ind += 1
        if parent2[paths[int(ind)][0]][paths[int(ind)][1]].GetHumans()<= max_humans:
            parent2[self.__position[0]][self.__position[1]].AddHuman(-1)
            self.__position = paths[ind]
            parent2[paths[int(ind)][0]][paths[int(ind)][1]].AddHuman(1)
        return(self.__position)

