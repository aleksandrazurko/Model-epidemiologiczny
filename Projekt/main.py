from sys import argv
from Graph import *
from Space import *
from Vertex import *
from Human import *
from Point import *
import random
import numpy as np
import matplotlib.pyplot as plt

space = argv[1] #nazwa pliku z pomieszczeniem
paths = argv[2] #nazwa pliku ze ścieżkami
steps = int(argv[3]) #liczba kroków
prob_in = int(argv[4]) #prawdopodobieństwo wejścia nowego człowieka
mask = float(argv[5]) #jaki % osób ma maseczkę
max_humans = int(argv[6]) #ile maksymalnie osób może znajdować się na polu
status_I = float(argv[7]) #jaki % osób ma być zarażonych na wejściu
virus = float(argv[8]) #ile wirusa zostawia osoba zarażona
virus_death = float(argv[9]) #jaki % wirusa umiera w jednym kroku
virus_trans = float(argv[10]) #jaki % wirusa jest przekazywany do sąsiadów
prob_I = float(argv[11]) #jaki jest przelicznik na zarażenie w zależności od stężenia wirusa
max_prob_I = float(argv[12]) #jakie jest maksymalne prawdopodobieństwo zarażenia
factor_mask = float(argv[13]) #ile razy mniejsze jest prawdopodobieństwo zarażenia w maseczce

o = Object() #tworzenie Obiektu
o.ReadObject(space) #wczytanie pliku z pomieszczeniam przez Obiekt

g = Graph() #tworzenie Grafu
g.ReadGraph(paths) #wczytanie pliku ze ścieżkami przez Graf

#wywołanie ruchu ludzi z wczytanymi parametrami, zwracana jest lista kroków (x) oraz lista zarażeń w danym kroku (y)
x,y = o.Motion(g, steps,prob_in,max_humans,mask,virus,virus_death, virus_trans, status_I, factor_mask,prob_I, max_prob_I)

#testowe rysowanie wykresu ze zwróconymi danymi
plt.plot(x,y)
plt.xlabel('kroki')
plt.ylabel('zarażenia')
plt.show()
