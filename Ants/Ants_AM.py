import numpy as np
import matplotlib.pyplot as plt

class LangtonsAnt():
    
    def __init__(self, m, n, position, direction):
        self.__m = int(m)
        self.__n = int(n)
        self.__position = position
        self.__direction = direction
        self.__board = np.zeros((m,n))

    def Go(self, steps):
        coord_moves = {
            "R": {(0, -1): (-1, 0), (-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1)},
            "L": {(0, -1): (1, 0), (1, 0): (0, 1), (0, 1): (-1, 0), (-1, 0): (0, -1)},
        }
        for i in range (steps):
            field = self.__board[self.__position[1]][self.__position[0]]
            L_R = "L" if field else "R"
            self.__direction = coord_moves[L_R][self.__direction]
            self.__board[self.__position[1]][self.__position[0]] = 0 if field else 1
            self.__position[1],self.__position[0] = self.__position[1] + self.__direction[0], self.__position[0]+self.__direction[1]
    def Draw(self):
        plt.imshow(self.__board,cmap = 'rainbow', interpolation ='nearest')
        plt.show()
        


ant1 = LangtonsAnt(11,11, [5,5], (0,-1))
ant1.Go(200)
ant1.Draw()
