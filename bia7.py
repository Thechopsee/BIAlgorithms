
import copy
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction
from Renderer import Render

class Solution:
    def __init__(self,lower_bound, upper_bound, number_of_individuals, number_of_gen_cycles):
        self.dimension = 2
        self.draw = []
        self.lB = lower_bound  
        self.uB = upper_bound
        self.NP = number_of_individuals
        self.M_max = number_of_gen_cycles
        self.PRT = 0.4
        self.path_length = 3
        self.step = 0.11
        self.f = np.inf

    def generatePop(self):
        pop = []
        for i in range(self.NP):
            x=np.random.uniform(self.lB,self.uB)
            y=np.random.uniform(self.lB,self.uB)
            pop.append([x,y])
        return pop

    def findLeader(self, pop, fnc):
        personalBest = fnc(pop[0][0],pop[0][1])
        personalBestSave=pop[0]
        for i,particle in enumerate(pop):
            if(personalBest > fnc(particle[0],particle[1])):
                personalBest = fnc(particle[0],particle[1])
                personalBestSave=copy.deepcopy(particle)

        return personalBestSave

    def soma(self, fnc):
        pop = self.generatePop()
        leader = self.findLeader(pop, fnc)
        m = 0
        while m < self.M_max:
            leader = self.findLeader(pop, fnc)
            for i in range(len(pop)):
                pop[i] = self.recalculateIndividual(pop[i], leader, fnc)
            self.draw.append(copy.deepcopy(pop))
            m += 1
        return pop

    def boundaries(self,vector):
            for i in range(len(vector)):
                if(vector[i] > self.uB):
                    vector[i] = self.uB
                elif (vector[i] < self.lB):
                    vector[i] = self.lB
            return vector

    def recalculateIndividual(self, individual, leader, fnc):
        old = copy.deepcopy(individual)
        new = copy.deepcopy(individual)
        partialIndividual = copy.deepcopy(individual)
        count = self.step
        while count < self.path_length:
            for x in range(self.dimension):
                if np.random.uniform(0, 1) < self.PRT:
                    prtVector = 1
                else:
                    prtVector = 0
                new[x] = np.add(old[x], np.multiply(np.subtract(leader[x], old[x]), (count*prtVector)))

            new = self.boundaries(new)

            if(fnc(new[0],new[1]) < fnc(partialIndividual[0],partialIndividual[1])):
                partialIndividual = copy.deepcopy(new)
            count += self.step

        if (fnc(partialIndividual[0],partialIndividual[1]) < fnc(old[0],old[1])):
            return partialIndividual
        else:
            return old

gens=20
sf=SphereFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=SchwefelFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=RosenbrockFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=RastriginFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=GriewankFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=LevyFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=MichalewiczFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=ZakharovFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=AckleyFunction()          
solution = Solution(sf.lb,sf.ub,20,gens)
solution.soma(sf.useF)
r=Render()
r.runanim(solution.draw,sf)
