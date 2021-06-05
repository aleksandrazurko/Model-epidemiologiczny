'''Towrzenie pliku z wynikami symulacji
n_loop... ilosc przeprowadzonych symulacji
steps...ilosc wykonanych kroków podczas symulacji
prob_in...prawdopodobieństwo wejscia do pomieszczenia
max_humans...maksymalna ilosc osob na wejsciu
mask...prawdopobienstwo na noszenie maski
virus...ilosc wirusa
virus_death...umieralnosc wirusa    
virus_trans...rozprzstrzenianie sie wirusa
prob_I...prawdopodobienstwo zarazenia
factor_mask...czynnik maski
factor_I...czynnik zarazenia
max_prob_I...maksymalne prawdopodobienstwo zarazenia'''
from Graph import *
from Space import *
from Vertex import *
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import time
#from main import *
import os.path
start_time = time.time() 

n_loop=100

space = 'gym.txt'
paths = 'gym_path.txt'
steps=100
prob_in = float(5)
max_humans=float(1)
mask = float(0)
status_I = float(5)
virus = float(1)
virus_death = float(10)
virus_trans = float(20)
max_prob_I = float(96)
factor_mask = float(5)
prob_I=float(0.1)
keep = 'zatrzymanie-10_krokow.txt'
#parametry = {'mask':[0., 10., 30., 50., 70., 80., 90., 100.], 'prob_in':[1.,10., 20., 30., 40., 50., 60., 70.], 'status_I':[1., 5., 10., 15., 20., 30., 40., 50.]}
parametry = {'prob_in':[1.,10., 20., 30., 40., 50., 60., 70.], 'virus_death':[1.,10., 20., 50.], 'mask':[0., 10., 30., 50., 70., 80., 90., 100.], 'status_I':[1., 5., 10., 15., 20., 30., 40., 50.], 'virus_trans':[1., 10., 20., 30., 50.], 'prob_I':[0.05, 0.1, 0.5, 0.7], 'factor_mask':[1.5, 2., 3., 5., 10.]}


def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Time Lapsed = {0}:{1}:{2}".format(int(hours),int(mins),sec))


for par in parametry:
    for zmienna in parametry[par]:
        typ=space[0]
        o = Object()
        o.ReadObject(space)

        g = Graph()
        g.ReadGraph(paths)

        if space == 'sklep_zespolowe.txt' and keep:
            o.RelevantPlaces(keep)
        else:
            keep = []

        if par == 'prob_in':    
            param=[typ,steps,zmienna,max_humans,mask,virus,virus_death, virus_trans, status_I, factor_mask,prob_I,max_prob_I]
            name=",".join(map(str,param))+'.txt'

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths)
                
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, zmienna, max_humans, mask, virus, virus_death, virus_trans,status_I, factor_mask, prob_I, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths)                    
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, zmienna, max_humans, mask, virus, virus_death, virus_trans,status_I, factor_mask, prob_I, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)            


        elif par == 'mask':
            param=[typ,steps,prob_in,max_humans,zmienna,virus,virus_death, virus_trans, status_I, factor_mask,prob_I,max_prob_I]
            name=",".join(map(str,param))+'.txt'

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths)  
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, zmienna, virus, virus_death, virus_trans,status_I, factor_mask, prob_I, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths)  
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, zmienna, virus, virus_death, virus_trans,status_I, factor_mask, prob_I, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)   


        elif par == 'virus_death':
            param=[typ,steps,prob_in,max_humans,mask,virus,zmienna, virus_trans, status_I, factor_mask,prob_I,max_prob_I]
            name=",".join(map(str,param))+'.txt'

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths)  
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, zmienna, virus_trans,status_I, factor_mask, prob_I, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths) 
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, zmienna, virus_trans,status_I, factor_mask, prob_I, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)    


        elif par == 'virus_trans':
            param=[typ,steps,prob_in,max_humans,mask,virus,virus_death, zmienna, status_I, factor_mask,prob_I,max_prob_I]
            name=",".join(map(str,param))+'.txt'

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths) 
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, zmienna,status_I, factor_mask, prob_I, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths) 
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, zmienna,status_I, factor_mask, prob_I, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)       


        elif par == 'status_I':
            param=[typ,steps,prob_in,max_humans,mask,virus,virus_death, virus_trans, zmienna, factor_mask,prob_I,max_prob_I]
            name=",".join(map(str,param))+'.txt'

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths) 
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, virus_trans,zmienna, factor_mask, prob_I, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths) 
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, virus_trans,zmienna, factor_mask, prob_I, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)               


        elif par == 'factor_mask':
            param=[typ,steps,prob_in,max_humans,mask,virus,virus_death, virus_trans, status_I, zmienna,prob_I,max_prob_I]
            name=",".join(map(str,param))+'.txt'

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths) 
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, virus_trans,status_I, zmienna, prob_I, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths) 
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, virus_trans,status_I, zmienna, prob_I, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)   


        elif par == 'prob_I':
            param=[typ,steps,prob_in,max_humans,mask,virus,virus_death, virus_trans, status_I, factor_mask,zmienna,max_prob_I]
            name=",".join(map(str,param))+'.txt'            

            if os.path.isfile(name):
                plik = open(name, "at")
            else:
                plik = open(name, "at")
                Name=name.strip('.txt').split(',')
                plik.writelines(['typ=',Name[0],'\nsteps=',Name[1],'\nprob_in=',Name[2],'\nmax_humans=',Name[3],'\nmask=',Name[4],'\nvirus=',Name[5],'\nvirus_death=',Name[6],'\nvirus_trans=',Name[7],'\nstatus_I=',Name[8],'\nfactor_mask=',Name[9],'\nfactor_I=',Name[10],'\nmax_prob_I=',Name[11]])
                plik.write('\n')
            if n_loop==1:
                o = Object()
                o.ReadObject(space)
                g = Graph()
                g.ReadGraph(paths) 
                number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, virus_trans,status_I, factor_mask, zmienna, max_prob_I, keep)
                WYNIKI=[we,iI,stanI[-1],wy,mc]
                WYNIKI=",".join(map(str,WYNIKI))
                plik.write(WYNIKI)
                plik.write('\n')
            else:
                for k in range(n_loop):
                    ''' z symulacji otrzymamy:
                    we... ilosc osób na wejsciu
                    iI... ilosc chorych na wejsciu
                    stanI[-1]... ilosc osob zarażonych na wyjsciu
                    wy... ilosc osob na wyjsciu
                    mc... ilosc osob w maskach'''
                    o = Object()
                    o.ReadObject(space)
                    g = Graph()
                    g.ReadGraph(paths) 
                    number_step, stanI, mc, iI, we, wy = o.Motion(g, steps, prob_in, max_humans, mask, virus, virus_death, virus_trans,status_I, factor_mask, zmienna, max_prob_I, keep)
                    WYNIKI=[we,iI,stanI[-1],wy,mc]
                    WYNIKI=",".join(map(str,WYNIKI))
                    plik.write(WYNIKI)
                    plik.write('\n')
            plik.close()

            end_time = time.time()
            time_convert(end_time - start_time)   
