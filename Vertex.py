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
        
    #zwracanie wspolrzednych wierzchołka
    def GetVertex(self):
        return(self.__coordinate)

    #zwracanie dostepnych ścieżek z wierzchołka
    def GetPath(self):
        return(self.__path)

    #zwracanie prawdopodobieństwa wyboru danej ścieżki
    def GetProbability(self):
        return(self.__probability)
