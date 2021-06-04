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
# space = 'sklep_zespolowe.txt'
# paths = 'sklep_graf.txt'
steps = 400
prob_in = int(2)
mask = float(1)
max_humans = float(0)
status_I = float(10)
virus = float(1)
virus_death = float(10)
virus_trans = float(20)
prob_I = float(0.1)
max_prob_I = float(95)
factor_mask = float(5)
keep = 'zatrzymanie-10_krokow.txt'
gym = True


# space = argv[1]
# paths = argv[2]
# steps = int(argv[3])
# prob_in = int(argv[4])
# mask = float(argv[5])
# max_humans = float(argv[6])
# status_I = float(argv[7])
# virus = float(argv[8])
# virus_death = float(argv[9])
# virus_trans = float(argv[10])
# prob_I = float(argv[11])
# max_prob_I = float(argv[12])
# factor_mask = float(argv[13])
# keep = argv[14]
# gym = argv[15]

o = Object()
o.ReadObject(space)


g = Graph()
g.ReadGraph(paths)


if space == 'sklep_zespolowe.txt' and keep:
    o.RelevantPlaces(keep)
else: keep = []

x,y = o.Motion(g, steps,prob_in,max_humans,mask,virus,virus_death, virus_trans, status_I, factor_mask,prob_I, max_prob_I, keep, gym)
plt.plot(x,y)
plt.xlabel('kroki')
plt.ylabel('zarażenia')
plt.show()
