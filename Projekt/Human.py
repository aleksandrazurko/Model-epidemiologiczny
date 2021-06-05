from Graph import *
from Space import *
from Vertex import *
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import pygame as pg

class Human():
    #konstruktor
    def __init__(self,position, status, mask): 
        self.__position = position #pozycja człowieka
        self.__status = status #status człowieka
        self.__mask = mask #czy posiada maseczkę
        self.__stop = 0
        self.__wait = 0 #timer for frozing person

    #destruktor
    def __del__(self):
        return()

    #zmiana statusu
    def ChangeStatus(self, new_status):
        self.__status = new_status

    #zwracanie pozycji
    def GetPosition(self):
        return(self.__position)

    def IsWaiting(self):
        return(self.__wait>0)


    #zwracanie statusu
    def GetStatus(self):
        return(self.__status)

    #zwracanie maseczki true/false
    def GetMask(self):
        return(self.__mask)

    #wykonanie kroku
    def Step(self, graph,grid, max_humans):
        if self.__wait>0:
            self.__wait-=1
        else:
            path = graph.GetPath(self.__position)
            if grid[int(path[0])][int(path[1])].GetHumans() < max_humans:
                grid[int(self.__position[0])][int(self.__position[1])].AddHuman(-1)
                self.__position = path
                grid[int(path[0])][int(path[1])].AddHuman(1)
                if grid[int(path[0])][int(path[1])].GetType()==6:
                    self.__wait = 20
                elif grid[int(path[0])][int(path[1])].GetType()==3:
                    self.__wait = 5          
        return(self.__position)
