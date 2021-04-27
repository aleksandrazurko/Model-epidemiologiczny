import random

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
                    else:
                        try:
                            line[i] = int(line[i])
                        except:
                            print("Coordinates should be numeric")
                        temp_pr.append(line[i])
            if j%3 == 2: #pobieranie prawdopodobieństwa + tworzenie obiektu wierzchołek i dodanie go do listy w Graphie
                vertex = Vertex(temp_v, temp_pa, temp_pr)
                self.__vertices.append(vertex)
                print('Wczytane dane: ', vertex, '\n')
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

    def __str__(self):
        return('sciany: ' + str(self.__object) + '\ndrzwi: ' + str(self.__doors) + '\nwyłączone miejsca: ' + str(self.__excludeds))

    #wczytanie pliku z OBIEKTEM do wizualizacji        
    def ReadObject(self, FileName):
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


class Human():
    #konstruktor
    def __init__(self,position): 
        self.__position = position
        self.__status = 'S'
        self.__mask = True

    #destruktor
    def __del__(self):
        print('Destructor called, Human deleted.')    

    #wykonanie kroku
    def Step(self, parent):
        paths, probability = g.GetBack(self.__position)
        los = random.random()
        suma = 0
        ind = 0
        for p in probability:
            if (p/100 + suma) > los:
                break
            else:
                suma += p/100
                ind += 1
        return(paths[int(ind)])

    #wykonanie całego ruchu
    def Motion(self, parent):
        move = True
        while move == True:
            temp = self.Step(parent)
            if temp == g.End():
                self.__del__()
                move = False
            elif g.Available(temp):
                self.__position = temp

#raport danych np. ile osob wyszło
''' def Report(self):
print(self.counter_in)
print(self.counter_out)'''
                

#main        
o = Object()
o.ReadObject('pokoj_new.txt')

g = Graph()
g.ReadGraph('graph_test.txt')

h = Human(g.Start())
h.Motion(g)
#h.Report()




    

