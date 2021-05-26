from sys import argv
from Graph import *
from Space import *
from Vertex import *
from Human import *
from Point import *
import random
import numpy as np
import matplotlib.pyplot as plt

space = 'gym.txt'
paths = 'gym_path.txt'
steps = 500
prob_in = float(10)
mask = float(1)
max_humans = 8
status_I = float(10)
virus = float(1)
virus_death = float(10)
virus_trans = float(20)
prob_I = float(0.1)
max_prob_I = float(95)
factor_mask = float(5)
factor_I=0.1

o = Object()
#o.ReadObject('sklep_zespolowe.txt')
o.ReadObject(space)

g = Graph()
#g.ReadGraph('sklep_graf.txt')
g.ReadGraph(paths)

x,y = o.Motion(g, steps,prob_in,max_humans,mask,virus,virus_death, virus_trans, status_I, factor_mask,factor_I,max_prob_I)
plt.plot(x,y)
plt.xlabel('kroki')
plt.ylabel('zarażenia')
plt.show()
o.Visual()
o.ConcentrationVirus()
