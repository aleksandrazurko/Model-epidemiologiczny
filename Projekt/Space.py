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
        self.__humans = []
        self.__actives = []
        self.__wejscie = []
        self.__wyjscie = []
        self.__grid = []
        self.__size = []

    def __str__(self):
        return('sciany: ' + str(self.__object) + '\ndrzwi: ' + str(self.__doors) + '\nwyłączone miejsca: ' + str(self.__excludeds) + '\nkasy: ' + str(self.__cashdesks))     

    def DrawPolygon(self,vertices,type_):
        #zaznaczenie konturów w gridzie
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
        return(self.__object, self.__doors, self.__excludeds, self.__cashdesks)  

    def ReadStop(self, FileName):
        file = open(FileName, 'r').read()
        lines = file.split('\n')
        points = []
        i = 0
        for line in lines:
            if i%2 == 0:
                line = line.split(',')
                x = int(line[0])
                y = int(line[1])
            else:
                line = line.split(' ')
                probs = np.arange(int(line[0]),int(line[1]))
                temp = random.sample(probs,1)
            self.__grid[x][y].ChangeStops(temp)
            i += 1
            
    def Gray(self,im):
        im = 255 * (im/im.max())
        w,h = im.shape
        ret = np.empty((w,h,3),dtype = np.uint8)
        ret[:,:,2] = ret[:,:,1] = ret[:,:,0] = im
        return ret

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
        dosc = 255 * dosc / dosc.max()
        dosc = self.Gray(dosc)
        return(dosc)
          
    def Motion(self, parent, steps, prob_in, max_humans, mask, vir,vir_d, vir_tr, stat_I, factor_mask, factor_I, max_prob_I):
        pg.init()
        scale = 50
        screen = pg.display.set_mode((self.__size[0]*scale,self.__size[1]*scale))
        for ex in self.__excludeds:
            pg.draw.polygon(screen,(255,255,255), ((ex[0][0]*scale,ex[0][1]*scale),(ex[1][0]*scale,ex[1][1]*scale),(ex[2][0]*scale,ex[2][1]*scale),(ex[3][0]*scale,ex[3][1]*scale)),1)
        for d in self.__doors:
            pg.draw.line(screen,(0,0,255),(d[0][0]*scale,d[0][1]*scale),(d[1][0]*scale,d[1][1]*scale),20)
        for cd in self.__cashdesks:
            pg.draw.polygon(screen,(255,0,255), ((cd[0][0]*scale,cd[0][1]*scale),(cd[1][0]*scale,cd[1][1]*scale),(cd[2][0]*scale,cd[2][1]*scale),(cd[3][0]*scale,cd[3][1]*scale)),1)
        for a in self.__actives:
            pg.draw.polygon(screen,(255,255,0), ((a[0][0]*scale,a[0][1]*scale),(a[1][0]*scale,a[1][1]*scale),(a[2][0]*scale,a[2][1]*scale),(a[3][0]*scale,a[3][1]*scale)),1)
        we = 0
        wy = 0
        I = 0
        IIn = 0
        number_step = []
        stanI = []
        I_temp = 0
        clock = pg.time.Clock()
        for i in range(steps):
            number_step.append(i+1)
            x = random.random()
            if x <= prob_in/100 and self.__grid[int(parent.Start()[0])][int(parent.Start()[1])].GetHumans()<=max_humans:
                if x <= prob_in/100 * stat_I/100:
                    status = 'I'
                    IIn += 1
                else:
                    status = 'S'
                if x <= (prob_in/100 * mask/100):
                    mask = True
                else:
                    mask = False
                if status == 'I' and mask == 'True': self.__grid[parent.Start()[0]][parent.Start()[1]].ChangeVirus(1/factor_mask)
                elif status == 'I' and mask == 'False': self.__grid[parent.Start()[0]][parent.Start()[1]].ChangeVirus(1)
                human = Human(parent.Start(), status, mask)
                self.__humans.append(human)
                we += 1
            j = 0
            positions_list = []
            new_step = []
            max_queue = 1
            for h in self.__humans:
                n = positions_list.count(h.GetPosition())
                positions_list.append(h.GetPosition())
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
                        h.ChangeStatus('I')
                        I += 1
                        I_temp += 1
                        if h.GetMask():
                            self.__grid[int(temp[0]+1)][int(temp[1]+1)].AddVirus(vir/factor_mask)
                        else:
                            self.__grid[int(temp[0]+1)][int(temp[1]+1)].AddVirus(vir)
                m = new_step.count(h.GetPosition())
                new_step.append(h.GetPosition())
                if h.GetStatus() == 'I':
                    pg.draw.circle(screen, (255, 0, 0), (h.GetPosition()[0] * scale, h.GetPosition()[1] * scale + m * 10), 5)
                else:
                    pg.draw.circle(screen, (100, 240, 50), (h.GetPosition()[0] * scale, h.GetPosition()[1] * scale + m * 10), 5)
                if temp == parent.End():
                    del h
                    del self.__humans[j]
                    wy += 1
                    self.__grid[int(temp[0])][int(temp[1])].AddHuman(-1)
                j += 1
                pg.display.update()
            self.__wejscie.append(we)
            self.__wyjscie.append(wy)
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
                                    try:
                                        self.__grid[m+mx][n+ny].AddVirus(temp)
                                    except:
                                        self.__grid[m][n].AddVirus(temp)
                                    ny += 1
                            mx += 1
            dosc = self.ConcentrationVirusVisual(scale)
            surf = pg.surfarray.make_surface(dosc)
            screen.blit(surf,(0,0))
            pg.display.update()
            for ex in self.__excludeds:
                pg.draw.polygon(screen,(255,255,255), ((ex[0][0]*scale,ex[0][1]*scale),(ex[1][0]*scale,ex[1][1]*scale),(ex[2][0]*scale,ex[2][1]*scale),(ex[3][0]*scale,ex[3][1]*scale)),1)
            for d in self.__doors:
                pg.draw.line(screen,(0,0,255),(d[0][0]*scale,d[0][1]*scale),(d[1][0]*scale,d[1][1]*scale),20)
            for cd in self.__cashdesks:
                pg.draw.polygon(screen,(255,255,255), ((cd[0][0]*scale,cd[0][1]*scale),(cd[1][0]*scale,cd[1][1]*scale),(cd[2][0]*scale,cd[2][1]*scale),(cd[3][0]*scale,cd[3][1]*scale)),1)
            for a in self.__actives:
                pg.draw.polygon(screen,(255,255,0), ((a[0][0]*scale,a[0][1]*scale),(a[1][0]*scale,a[1][1]*scale),(a[2][0]*scale,a[2][1]*scale),(a[3][0]*scale,a[3][1]*scale)),1)
            pg.display.update()
            stanI.append(I_temp)
            demendedFps = 5
            clock.tick(demendedFps)
        pg.quit()
        return(number_step,stanI)         

    def Visual(self):
        x = np.arange(len(self.__wejscie))
        plt.plot(x,self.__wejscie)
        plt.plot(x,self.__wyjscie)
        plt.xlabel('krok')
        plt.ylabel('liczba ludzi')
        plt.legend(('wejscie', 'wyjscie'))
        plt.show()

    def ConcentrationVirus(self):
        matrix = np.zeros((self.__size[0],self.__size[1]))
        for i in range(self.__size[0]):
            for j in range(self.__size[1]):
                matrix[i][j] = self.__grid[i][j].GetVirus()
        plt.imshow(matrix)
        plt.show()
