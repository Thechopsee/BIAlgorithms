import copy
from time import sleep
from tkinter import Y
import matplotlib.pyplot as plt
import numpy as np

from Renderer import Render
from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction

class Solution:
    def __init__(self,lower_bound, upper_bound, number_of_individuals, number_of_gen_cycles):
        self.lB = lower_bound  
        self.uB = upper_bound
        self.NP = number_of_individuals
        self.Gmaxim = number_of_gen_cycles
        self.F = 0.5
        self.CR = 0.5 
        self.funkce=None
        self.draw = []


    def boundaries(self,vector):
            for i in range(len(vector)):
                if(vector[i] > self.uB):
                    vector[i] = self.uB
                elif (vector[i] < self.lB):
                    vector[i] = self.lB

    def differentialEvolution(self,funkce):
        self.funkce=funkce
        actual_pop = self.generateSused()
        g = 0
        while g < self.Gmaxim:
            new_pop = copy.deepcopy(actual_pop)
            for i, x in enumerate(actual_pop):
                r1,r2,r3 = i,i,i
                while r1==i:
                    r1 = np.random.randint(0, self.NP)
                while 1:
                    r2 = np.random.randint(0, self.NP)
                    if (r2 != i and r2 != r1):
                        break
                while 1:
                    r3 = np.random.randint(0, self.NP)
                    if (r3 != i and r3 != r1 and r3 != r2):
                        break

                p = (np.subtract(actual_pop[r1], actual_pop[r2]))
                map(lambda k: k * self.F, p)
                v = np.add(p, actual_pop[r3])
                self.boundaries(v)
                u = np.zeros(2) 
                rand = np.random.randint(0, 2)
                for j in range(2):
                    if np.random.uniform() < self.CR or j == rand:
                        u[j] = v[j]
                    else:
                        u[j] = actual_pop[i][j]
                f_u = funkce.useF(u[0],u[1])

                if f_u <= funkce.useF(actual_pop[i][0],actual_pop[i][1]):
                     new_pop[i] = u
            actual_pop = new_pop
            self.draw.append(new_pop)
            g += 1
            

        return actual_pop

    def generateSused(self):
        susedi = []
        for x in range(self.NP):
            pi = []
            for y in range(2):
                pi.append(np.random.uniform(self.lB,self.uB))
            susedi.append(pi)
        return susedi


                

solution = Solution(-5.12,5.12,10,50)
sf=SphereFunction()
s=solution.differentialEvolution(sf)
r=Render()
r.runanim(solution.draw,sf)
