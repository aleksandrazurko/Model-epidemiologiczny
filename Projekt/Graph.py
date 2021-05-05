from Space import *
from Vertex import *
from Human import *
import random
import numpy as np
import matplotlib.pyplot as plt

class Graph():
    def __init__(self):
        self.__vertices = []

    #wczytywanie pliku z "grafem"    
    def ReadGraph(self, FileName):
        file = open(FileName, 'r').read()
        lines = file.split('\n')
        j = 0
        for line in lines:
            if j%3 == 0: #zerowanie tablic tymczasowych, pobranie współrzędnych wierzchołka
                temp_v = []
                temp_pa = []
                temp_pr = []
                line_temp = line.split(',')
                try:
                    line_temp[0] = int(line_temp[0])
                    line_temp[1] = int(line_temp[1])
                except:
                    print("Coordinates should be numeric")
                temp_v.append(line_temp[0])
                temp_v.append(line_temp[1])
            else:
                line = line.split(' ')
                for i in range(int((len(line)))):
                    if j%3 == 1: #pobranie współrzędnych możliwych punktów
                        line_temp = line[i].split(',')
                        try:
                            line_temp[0] = int(line_temp[0])
                            line_temp[1] = int(line_temp[1])
                        except:
                            print("Coordinates should be numeric")
                        temp_pa.append([line_temp[0],line_temp[1]])
                    else: #pobieranie prawdopodobieństwa
                        try:
                            line[i] = int(line[i])
                        except:
                            print("Coordinates should be numeric")
                        temp_pr.append(line[i])
                        
            if j%3 == 2: #tworzenie obiektu wierzchołek i dodanie go do listy w Graphie
                vertex = Vertex(temp_v, temp_pa, temp_pr)
                self.__vertices.append(vertex)
                #print('Wczytane dane: ', vertex, '\n')
            j += 1

    #zwracanie współrzędnych punktu startowego          
    def Start(self):
        return(self.__vertices[0].GetVertex())

    #zwracanie współrzędnych końca chodzenia
    def End(self):
        return(self.__vertices[-1].GetPath()[0])

    #zwracanie możliwych punktów oraz prawdopodobieństwa dla zadanego wierzchołka
    def GetBack(self,vertex):
        for i in range(len(self.__vertices)):
            if self.__vertices[i].GetVertex() == vertex:
                return(i, self.__vertices[i].GetPath(), self.__vertices[i].GetProbability())

    def Available(self, vertex,prev_vertex):
        return True
   
        
