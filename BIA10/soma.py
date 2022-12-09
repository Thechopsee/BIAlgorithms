
import copy
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3

from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction

class SOMASolution:
    def __init__(self,lower_bound, upper_bound, number_of_individuals, number_of_gen_cycles,dimension):
        self.dimension = dimension
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
        susedi = []
        for x in range(self.NP):
            pi = []
            for y in range(self.dimension):
                pi.append(np.random.uniform(self.lB,self.uB))
            susedi.append(pi)
        return susedi

    def findLeader(self, pop, fnc):
        personalBest = fnc(pop[0],True)
        personalBestSave=pop[0]
        for i,particle in enumerate(pop):
            if(personalBest > fnc(particle,True)):
                personalBest = fnc(particle,True)
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

            if(fnc(new,True) < fnc(partialIndividual,True)):
                partialIndividual = copy.deepcopy(new)
            count += self.step

        if (fnc(partialIndividual,True) < fnc(old,True)):
            return partialIndividual
        else:
            return old



