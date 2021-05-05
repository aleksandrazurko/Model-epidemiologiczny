from Graph import *
from Space import *
from Vertex import *
from Human import *
import random
import numpy as np
import matplotlib.pyplot as plt

o = Object()
o.ReadObject('sklep_zespolowe.txt')

g = Graph()
g.ReadGraph('sklep_graf.txt')

x,y = o.Motion(g)
plt.plot(x,y)
plt.xlabel('kroki')
plt.ylabel('zarażenia')
plt.show()
o.Visual()
