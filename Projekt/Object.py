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
                return(self.__vertices[i].GetPath(), self.__vertices[i].GetProbability())

    def Available(self, position):
        return True


class Vertex():
    #konstruktor wierzchołka
    def __init__(self, coordinate, path, probability):
        self.__coordinate = coordinate
        self.__path = path
        self.__probability = probability
        
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
   

class Object():
    #konstruktor
    def __init__(self):
        self.__object = []
        self.__doors = []
        self.__excludeds = []
        self.__humans = []
        self.__wejscie = []
        self.__wyjscie = []
        self.__grid = []
        self.__size = []
        self.__I = []
        self.__IIn = []

    def __str__(self):
        return('sciany: ' + str(self.__object) + '\ndrzwi: ' + str(self.__doors) + '\nwyłączone miejsca: ' + str(self.__excludeds))

    #wczytanie pliku z OBIEKTEM do wizualizacji        
    def ReadObject(self, FileName):
        x = []
        y = []
        file = open(FileName, 'r').read()
        lines = file.split('\n')
        for line in lines:
            line = line.split(' ')
            for i in range(int((len(line)-1))):
                line_temp = line[i+1].split(',')
                try:
                    line_temp[0] = int(line_temp[0])
                    line_temp[1] = int(line_temp[1])
                except:
                    print("Coordinates should be numeric")
                if line[0] == 'object':
                    self.__object.append([line_temp[0],line_temp[1]])
                elif line[0] == 'door':
                    self.__doors.append([line_temp[0],line_temp[1]])
                elif line[0] == 'excluded':
                    self.__excludeds.append([line_temp[0],line_temp[1]])
                elif line[0] == 'size':
                    self.__size.append(line_temp[0])
                    self.__size.append(line_temp[1])
        for i in range(len(self.__object)):
            x.append(int(self.__object[i][0]))
            y.append(int(self.__object[i][1]))
      

    def Motion(self, parent):
        we = 0
        wy = 0
        I = 0
        IIn = 0
        grid = np.zeros((self.__size[0], self.__size[1]))
        error = 0
        number_step = []
        stanI = []
        I_temp = 0
        for i in range(10000):
            number_step.append(i+1)
            x = random.random()
            #I_temp = 0
            if x < 0.3:
                if x <= 0.29: status = 'S'
                else:
                    status = 'I'
                    grid[parent.Start()[0]][parent.Start()[1]] += 1
                    IIn+=1
                    #I_temp += 1
                if x <= 0.29:
                    mask = True
                else:
                    mask = False
                human = Human(parent.Start(), status, mask)
                self.__humans.append(human)
                we += 1
            j = 0
            for h in self.__humans:
                temp = h.Step(parent)
                if h.GetStatus() == 'I':
                    grid[temp[0]][temp[1]] += 1
                if grid[temp[0]][temp[1]] != 0 and h.GetStatus() == 'S':
                    risk = random.random()
                    if grid[temp[0]][temp[1]]*0.1 <= 0.9:
                        prob = grid[temp[0]][temp[1]]*0.1
                    else:
                        prob = 0.95
                    if risk <= prob:
                        h.ChangeStatus('I')
                        I += 1
                        I_temp += 1
                        grid[temp[0]][temp[1]] += 1
                if temp == parent.End():
                    del h
                    del self.__humans[j]
                    wy += 1
                j += 1
            self.__wejscie.append(we)
            self.__wyjscie.append(wy)
            self.__I.append(I)
            for m in range(self.__size[0]):
                for n in range(self.__size[1]):
                    if grid[m][n] > 0:
                        new = 0.9 * grid[m][n]
                        temp = 0.2 * new/8
                        grid[m][n] = 0.8 * new
                        mx = -1
                        ny = -1
                        for mm in range(2):
                            for nn in range(2):
                                if ny != 0 and mx != 0:
                                    try:
                                        grid[m+mx][n+ny] += temp
                                    except:
                                        print('nie')
                                    ny += 1
                            mx += 1
            stanI.append(I_temp)
        print(grid)
        print(I)
        print(IIn)
        return(number_step,stanI)

                        
                    

    def Visual(self):
        x = np.arange(len(self.__wejscie))
        plt.plot(x,self.__wejscie)
        plt.plot(x,self.__wyjscie)
        plt.legend(('wejscie', 'wyjscie'))
        plt.show()

 
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

    def GetStatus(self):
        return(self.__status)

    #wykonanie kroku
    def Step(self, parent):
        paths, probability = parent.GetBack(self.__position)
        los = random.random()
        suma = 0
        ind = 0
        for p in probability:
            if (p/100 + suma) > los:
                break
            else:
                suma += p/100
                ind += 1
        if g.Available(paths[int(ind)]) == True:
            self.__position = paths[int(ind)]
        return(self.__position)


#raport danych np. ile osob wyszło
''' def Report(self):
print(self.counter_in)
print(self.counter_out)'''
                

#main

o = Object()
o.ReadObject('sklep_zespolowe.txt')

g = Graph()
g.ReadGraph('sklep_graf.txt')

x,y = o.Motion(g)
plt.plot(x,y)
plt.show()
o.Visual()





    

