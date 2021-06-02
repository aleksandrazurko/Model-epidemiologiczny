from Graph import *
from Vertex import *
from Human import *
from Point import *
import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame as pg

class Object():
    #konstruktor
    def __init__(self):
        self.__object = []
        self.__doors = []
        self.__excludeds = []
        self.__cashdesks = []
        self.__cashdesksinfX = []
        self.__cashdesksinfY = []
        self.__inwalls=[]
        self.__indoors=[]
        self.__humans = []
        self.__actives = []
        self.__wejscie = []
        self.__wyjscie = []
        self.__grid = []
        self.__size = []

    def DrawPolygon(self,vertices,type_):
        #zaznaczenie danych punktów w Gridzie, tj. gdzie znajdują się ściany, regały, recepcja itp.
        for i in range (len(vertices)):
            x = [vertices[i%len(vertices)][0],vertices[(i+1)%len(vertices)][0]]
            y = [vertices[i%len(vertices)][1],vertices[(i+1)%len(vertices)][1]]
            if y[0] != y[1] and x[0] != x[1]:
                a = (y[0]-y[1])/(x[0]-x[1])
                b = y[0] - a*x[0]
                j = 0
                x = sorted(x)
                while x[0]+j <= x[1]:
                    y_temp = (x[0] + j)*a + b
                    x_temp = int(round(x[0],0))
                    y_temp = int(round(y_temp,0))
                    (self.__grid[x_temp])[y_temp].ChangeType(type_)
                    j+=1
            elif y[0] == y[1]:
                j = 0
                x = sorted(x)
                while x[0]+j < x[1]:
                    (self.__grid[x[0]+j])[y[0]].ChangeType(type_)
                    j+=1
            elif x[0] == x[1]:
                y = sorted(y)
                j = 0
                while y[0]+j < y[1]:
                    (self.__grid[x[0]])[y[0]+j].ChangeType(type_)
                    j+=1
    
    #wczytanie pliku z OBIEKTEM do wizualizacji        
    def ReadObject(self, FileName):
        x = []
        y = []
        file = open(FileName, 'r').read()
        lines = file.split('\n')
        cashdesksinf0 = []
        for line in lines:
            temp_excluded = []
            temp_doors = []
            temp_cashdesks = []
            temp_cashdesksinfX = []
            temp_cashdesksinfY = []
            temp_active = []
            temp_inwalls=[]
            temp_indoors=[]
            line = line.split(' ')
            for i in range(int((len(line)-1))):
                line_temp = line[i+1].split(',')
                try:
                    line_temp[0] = int(line_temp[0])
                    line_temp[1] = int(line_temp[1])
                except:
                    if (line[0] == 'cashdesk' and line_temp[0] != 'above' and line_temp[0] != 'below') or line[0] != 'cashdesk':
                        print("Coordinates should be numeric")
     
                if line[0] == 'object':
                    self.__object.append([line_temp[0],line_temp[1]])
                elif line[0] == 'door':
                    temp_doors.append([line_temp[0],line_temp[1]])
                elif line[0] == 'excluded':
                    temp_excluded.append([line_temp[0],line_temp[1]])
                elif line[0] == 'cashdesk':
                    if i == 0:
                        cashdesksinf0.append(line_temp[0])
                    else:
                        temp_cashdesksinfX.append(line_temp[0])
                        temp_cashdesksinfY.append(line_temp[1])
                        temp_cashdesks.append([line_temp[0],line_temp[1]])
                elif line[0] == 'size':
                    self.__size.append(line_temp[0])
                    self.__size.append(line_temp[1])
                elif line[0] == 'active':
                    temp_active.append([line_temp[0],line_temp[1]])
                elif line[0] == 'inwalls':
                    temp_inwalls.append([line_temp[0],line_temp[1]])
                elif line[0] == 'indoors':
                    temp_indoors.append([line_temp[0],line_temp[1]])
            if line[0] == 'excluded':
                self.__excludeds.append(temp_excluded)
            elif line[0] == 'door':
                self.__doors.append(temp_doors)
            elif line[0] == 'cashdesk':
                self.__cashdesks.append(temp_cashdesks)
                self.__cashdesksinfX.append(temp_cashdesksinfX)
                self.__cashdesksinfY.append(temp_cashdesksinfY)
            elif line[0] == 'active':
                self.__actives.append(temp_active)
            elif line[0] == 'inwalls':
                self.__inwalls.append(temp_inwalls) 
            elif line[0] == 'indoors':
                self.__indoors.append(temp_indoors) 
        for i in  range (self.__size[0]+1):
            line_temp = []
            for j in range (self.__size[1]+1):
                line_temp.append(Point(0,0,0))
            self.__grid.append(line_temp)
        self.DrawPolygon(self.__object,0)
        for d in self.__doors:
            self.DrawPolygon(d,1)
        for e in self.__excludeds:
            self.DrawPolygon(e,2)
        for i in range(len(self.__cashdesks)):
            self.DrawPolygon(self.__cashdesks[i],3)
            if cashdesksinf0[i] == 'below':
                self.__cashdesksinfY[i] = max(self.__cashdesksinfY[i]) + 1
            elif cashdesksinf0[i] == 'above':
                self.__cashdesksinfY[i] = min(self.__cashdesksinfY[i]) - 1
            self.__cashdesksinfX[i] = [min(self.__cashdesksinfX[i]),max(self.__cashdesksinfX[i])]
        for iw in self.__inwalls:
            self.DrawPolygon(iw,4)
        return(self.__object, self.__doors, self.__excludeds, self.__cashdesks)  

    def GetSize(self):
        return self.__size
    
    #tworzenie odcieni szarości do zaznaczania stężenia   
    def Gray(self,im,maximum):
        im = 255 * (im/maximum)
        w,h = im.shape
        ret = np.empty((w,h,3),dtype = np.uint8)
        ret[:,:,2] = ret[:,:,1] = ret[:,:,0] = im
        return ret

    #tworzenie macierzy z szarościami odpowiadającymi stężeniom
    def ConcentrationVirusVisual(self,scale):
        dosc = np.zeros((self.__size[0]*scale,self.__size[1]*scale))
        next_x = 0
        next_y = 0
        for i in range(len(dosc)):
            for j in range(len(dosc[0])):
                if j != 0 and j%scale == 0:
                    next_y += 1
                dosc[i][j] = self.__grid[next_x][next_y].GetVirus()
            if i != 0 and i%scale == 0:
                next_x += 1
            next_y = 0
        matrix_color = self.Gray(dosc, dosc.max())
        return(matrix_color)

    #wizualizacja człowieka
    def VisualHuman(self,scale,screen,h,new_step):
        #m = new_step.count(h.GetPosition())
        if h.GetStatus() == 'I':
            pg.draw.circle(screen, (255, 0, 0), (int(h.GetPosition()[0] * scale), int(h.GetPosition()[1] * scale)), scale/5)
        else:
            pg.draw.circle(screen, (100, 240, 50), (int(h.GetPosition()[0] * scale), int(h.GetPosition()[1] * scale)), scale/5)
        pg.display.update()
        
    #wizualizacja macierzy z kolorami stężeń
    def VisualConcentration(self,scale,screen):
        matrix_color = self.ConcentrationVirusVisual(scale)
        surf = pg.surfarray.make_surface(matrix_color)
        screen.blit(surf,(0,0))
        pg.display.update()

    #wizualizacja tła, tj. scian, drzwi, recepcji, kas itp.
    def VisualBackground(self,scale,screen):
        for ex in self.__excludeds:
            pg.draw.polygon(screen,(255,255,255), ((ex[0][0]*scale,ex[0][1]*scale),(ex[1][0]*scale,ex[1][1]*scale),(ex[2][0]*scale,ex[2][1]*scale),(ex[3][0]*scale,ex[3][1]*scale)),1)
        for d in self.__doors:
            pg.draw.line(screen,(0,0,255),(d[0][0]*scale,d[0][1]*scale),(d[1][0]*scale,d[1][1]*scale),20)
        for cd in self.__cashdesks:
            pg.draw.polygon(screen,(255,255,255), ((cd[0][0]*scale,cd[0][1]*scale),(cd[1][0]*scale,cd[1][1]*scale),(cd[2][0]*scale,cd[2][1]*scale),(cd[3][0]*scale,cd[3][1]*scale)),1)
        for a in self.__actives:
            pg.draw.polygon(screen,(255,255,0), ((a[0][0]*scale,a[0][1]*scale),(a[1][0]*scale,a[1][1]*scale),(a[2][0]*scale,a[2][1]*scale),(a[3][0]*scale,a[3][1]*scale)),1)
        for w in self.__inwalls:
            pg.draw.line(screen,(255,255,255),(w[0][0]*scale,w[0][1]*scale),(w[1][0]*scale,w[1][1]*scale),3) 
        for iD in self.__indoors:
            pg.draw.line(screen,(0,0,255),(iD[0][0]*scale,iD[0][1]*scale),(iD[1][0]*scale,iD[1][1]*scale),3)
        pg.display.update()

    #ruch wirusa, jego przekazywanie do sąsiadów oraz umieranie
    def MotionVirus(self,vir_d,vir_tr):
        for m in range(self.__size[0]+1):
            for n in range(self.__size[1]+1):
                if self.__grid[m][n].GetVirus() > 0:
                    new = (1 - vir_d/100) * self.__grid[m][n].GetVirus()
                    temp = vir_tr/100 * new/8
                    self.__grid[m][n].ChangeVirus(0.8 * new)
                    mx = -1
                    ny = -1
                    for mm in range(2):
                        for nn in range(2):
                            if ny != 0 and mx != 0:
                                if self.__grid[m+mx][n+ny].GetType() == 4:
                                    self.__grid[m][n].AddVirus(temp)
                                else:
                                    try:
                                        self.__grid[m+mx][n+ny].AddVirus(temp)
                                    except:
                                        self.__grid[m][n].AddVirus(temp)
                            ny += 1
                        mx += 1

    #główna funkcja, tworzenie ludzi, ruch ludzi, wywołanie ruchu wirusa, wywołanie wizualizacji          
    def Motion(self, parent, steps, prob_in, max_humans, mask, vir,vir_d, vir_tr, stat_I, factor_mask, factor_I, max_prob_I):
        pg.init()
        scale = 30 #powiększenie oknia wizualizacji
        screen = pg.display.set_mode((self.__size[0]*scale,self.__size[1]*scale))
        we = 0 #liczba osób, która weszła
        wy = 0 #liczba osób, która wyszła
        number_step = [] #lista z liczbą kroków
        stanI = [] #lista z zarażonymi w danym kroku
        I_temp = 0 #tymczasowa zmienna do zliczania zarażeń w danym kroku
        clock = pg.time.Clock()
        for i in range(steps):
            number_step.append(i+1)
            x = random.random() #losowanie z przedziału (0,1)
            #ustalenie czy człowiek wchodzi w danym kroku
            if x <= prob_in/100 and self.__grid[int(parent.Start()[0])][int(parent.Start()[1])].GetHumans()<=max_humans:
                #na podstawie prawdopodobieństwa podanego w argumencie Motion ustalanie statusu człowieka oraz czy dany człowiek posiada maseczkę
                if x <= prob_in/100 * stat_I/100:
                    status = 'I'
                else:
                    status = 'S'
                if x <= (prob_in/100 * mask/100):
                    mask = True
                else:
                    mask = False
                #w zależności od stanu i posiadania/braku maseczki wchodzącego człowieka ustalanie ile wirusa jest na wejściu
                if status == 'I' and mask == 'True': self.__grid[parent.Start()[0]][parent.Start()[1]].ChangeVirus(vir/factor_mask)
                elif status == 'I' and mask == 'False': self.__grid[parent.Start()[0]][parent.Start()[1]].ChangeVirus(vir)
                #tworzenie człowieka
                human = Human(parent.Start(), status, mask)
                #dodawanie obiektu human do listy ze wszystkimi powstałymi obiektami 
                self.__humans.append(human)
                we += 1
            j = 0
            new_step = []
            max_queue = 0
            #robienie kroku każdym człowiekiem, zmienianie stężenia wirusa w gridzie na podstawie statusu człowieka
            for h in self.__humans:
                self.VisualHuman(scale,screen,h,new_step)
                if h.GetPosition()[0] in self.__cashdesksinfY:
                    for i in range(len(self.__cashdesksinfY)):
                        if h.GetPosition()[0] == self.__cashdesksinfY[i] and h.GetPosition()[1] in range(self.__cashdesksinfX[i][0],self.__cashdesksinfX[i][1]+1):
                            temp = h.Step(parent,self.__grid, max_queue)
                        else: temp = h.Step(parent,self.__grid, max_humans)
                else: temp = h.Step(parent,self.__grid, max_humans)
                if h.GetStatus() == 'I':
                    if h.GetMask(): self.__grid[int(temp[0])][int(temp[1])].AddVirus(vir/factor_mask)
                    else: self.__grid[int(temp[0])][int(temp[1])].AddVirus(vir)
                if self.__grid[int(temp[0])][int(temp[1])].GetVirus() != 0 and h.GetStatus() == 'S':
                    risk = random.random()
                    if h.GetMask():
                        factor = factor_mask
                    else:
                        factor = 1
                    if self.__grid[int(temp[0]+1)][int(temp[1]+1)].GetVirus()*factor_I <= (max_prob_I/100)/factor:
                        prob = self.__grid[int(temp[0]+1)][int(temp[1]+1)].GetVirus()*factor_I
                    else:
                        prob = (max_prob_I/100)/factor
                    if risk <= prob:
                        h.ChangeStatus('IS')
                        I_temp += 1
                new_step.append(h.GetPosition())
                #self.VisualHuman(scale,screen,h,new_step)
                #pg.display.update()
                #usuwanie człowieka z listy oraz obiektu gdy dojdzie do wyjścia
                if temp == parent.End():
                    del self.__humans[j]
                    del h
                    wy += 1
                    self.__grid[int(temp[0])][int(temp[1])].AddHuman(-1)
                else:
                    j+=1
                #pg.display.update()
            self.__wejscie.append(we)
            self.__wyjscie.append(wy)
            self.MotionVirus(vir_d,vir_tr)
            stanI.append(I_temp)
            self.VisualConcentration(scale,screen)
            self.VisualBackground(scale,screen)
            #liczba klatek na sekundę - opóźnienie/przyspieszenie wizualizacji
            demendedFps = 50
            clock.tick(demendedFps)
        pg.quit()
        return(number_step,stanI) 
