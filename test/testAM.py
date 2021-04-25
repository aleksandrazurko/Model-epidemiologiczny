import random
import numpy as np

class Object():

    def __init__(self):
        self.__object = []
        self.__doors = []
        self.__excludeds = []
        self.__humans = []
        
    def Read(self, FileName):
        file = open(FileName, 'r').read()
        lines = file.split('\n')
        print(lines)
        for line in lines:
            line = line.split(' ')
            print(line)
            if line[0] == 'object':
                print('obiekt')
                for i in range(int((len(line)-1))):
                    line_temp = line[i+1].split(',')
                    print(line_temp)
                    try:
                        line_temp[0] = int(line_temp[0])
                        line_temp[1] = int(line_temp[1])
                    except:
                        print("Coordinates should be numeric")
                    self.__object.append([line_temp[0],line_temp[1]])
            elif line[0] == 'door':
                print('drzwi')
                door = Doors(line)
                self.__doors.append(door)
            elif line[0] == 'excluded':
                excluded = Excludeds(line)
                self.__excludeds.append(excluded)

    def Start(self):
        start = random.sample(self.__doors,1)
        return(start[0].Entry())
    
    def LinearFunction(self, p, q):
        if p[0] != q[0]:
            a = (p[1]-q[1])/(p[0]-q[0])
            b = p[1] - a * p[0]
        elif p[0] == q[0]:
            a = 0
            b = 0
        elif p[1] == q[1]:
            a = 0
            b = p[1]
        ab = (a, b)
        return ab
    
    def VerifyTriangle(self, a, b, c, p):
        triangle = (a, b, c)
        for j in range (len(triangle)):
            s = triangle[j]
            q = triangle[(j+1) % len(triangle)] #umozliwia wziecie pierwszego i ostatniego punktu
            ab = self.LinearFunction (s, q)
            a = ab[0]
            b = ab[1]
            #inny wierzcholek niz poprzednie:
            x = triangle[(j+2)%len(triangle)][0]
            y = triangle[(j+2)%len(triangle)][1]
            if a != 0:
                if y < a*x+b and p[1] > a*p[0]+b or y > a*x+b and p[1] < a*p[0]+b:
                    return False
                    break
            elif a == 0 and b == 0:
                if x < triangle[j][0] and p[0] > triangle[j][0] or x > triangle[j][0] and p[0] < triangle[j][0]:
                    return False
                    break
            elif a == 0 and b != 0:
                if y < b and p[1] > b or y > b and p[0] < b:
                    return False
                    break
            if j == len(triangle)-1:
                return True

    def PolygonChecker(self, vertices, point):
        
        first = 0
        last = len(vertices)-1
        lenght = len(vertices)
        while last - first > 2:
            mid = int (first + lenght/2)
            ab = self.LinearFunction(vertices[first], vertices[mid])
            a = ab[0]
            b = ab[1]
            if vertices[first+1][1] < a*vertices[first+1][0]+b and point[1] > a*point[0]+b or vertices[first+1][1] > a*vertices[first+1][0]+b and point[1] < a*point[0]+b:
                first = mid
                last = first
                lenght = lenght - lenght/2 + 1
            else:
                last = mid
                lenght = lenght/2 + 1
        return(self.VerifyTriangle(vertices[first], vertices[first+1], vertices[last], point))    

    def Available(self, point):
        #print(self.__object)
        return (self.PolygonChecker(self.__object,point))


class Excludeds():
    def __init__(self, line):
        self.__coordinates = []
        for i in range(int((len(line)-1))):
            line_temp = line[i+1].split(',')
            try:
                line_temp[0] = int(line_temp[0])
                line_temp[1] = int(line_temp[1])
            except:
                print("Coordinates should be numeric")
            self.__coordinates.append([line_temp[0],line_temp[1]])
        
class Doors():
    def __init__(self,line):
        self.__coordinates = []
        for i in range(int((len(line)-1))):
            line_temp = line[i+1].split(',')
            print('line',line_temp)
            try:
                line_temp[0] = int(line_temp[0])
                line_temp[1] = int(line_temp[1])
            except:
                print("Coordinates should be numeric")
            self.__coordinates.append([line_temp[0],line_temp[1]])
    def Entry(self):
        return(self.__coordinates[-1])

class Human():
    def __init__(self,position):
        self.__position = position
        self.__status = 'S'
        #print(position)
    def Step(self, parent):
        directions = ([0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[-1,1],[1,-1])
        direction = random.sample(directions,1)
        temp = [self.__position[0]+direction[0][0],self.__position[1]+direction[0][1]]
        print(temp)
        print(self.__position)
        if o.Available(temp): self.__position = temp
        print(self.__position)
        
        

o = Object()
o.Read("pokoj_new.txt")
h = Human(o.Start())
print('GO')
h.Step(o)
h.Step(o)
h.Step(o)
h.Step(o)
