from Graph import *
from Space import *
from Human import *
import random
import numpy as np
import matplotlib.pyplot as plt

class Vertex():
    #konstruktor wierzchołka
    def __init__(self, coordinate, path, probability):
        self.__coordinate = coordinate
        self.__path = path
        self.__probability = probability
        self.__available = True
        
    def __str__(self):
        text = 'wierzcholek: ' + str(self.__coordinate)
        for i in range (len(self.__path)):
            text += '\nmożliwość: ' + str(self.__path[i]) + ', prawdopodobieństwo: ' + str(self.__probability[i])
        return(text)

    def GetVertex(self):
        return(self.__coordinate)
    
    def GetPath(self):
        return(self.__path)
    
    def GetProbability(self):
        return(self.__probability)

    def ChangeAvailable(self, available):
        self.__available = available

    def GetAvailable(self):
        return(self.__available)
