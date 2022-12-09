import copy
from time import sleep

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import mpl_toolkits.mplot3d.axes3d as p3
from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction

class FASolution:
    def __init__(self,lower_bound, upper_bound, number_of_individuals, number_of_gen_cycles,dimensions):
        self.draw = []
        self.dimension = dimensions
        self.lB = lower_bound  
        self.uB = upper_bound
        self.NP = number_of_individuals
        self.g_maxim = number_of_gen_cycles
        self.gamma = 0.5
        self.alpha = (upper_bound-lower_bound)/150
        self.parameters = np.zeros(2)  

    def firefly(self, fnc):
        fireflies = self.generateSwarm()
        best_firefly_index = self.getBestFireflyIndex(fireflies, fnc)
        self.draw.append(copy.deepcopy(fireflies))
        t = 0
        while t < self.g_maxim:
            for i in range(self.NP):
                for j in range(self.NP):
                    if(i == j or i == best_firefly_index):
                        continue
                    dist = self.getEucleidianDistance(fireflies[i], fireflies[j])
                    first = fnc(fireflies[i],True)* np.e**(-self.gamma*dist)
                    second= fnc(fireflies[j],True)* np.e**(-self.gamma*dist)
                    if second < first:
                        fireflies[i]=self.moveFireflyThisTowards(fireflies[i], fireflies[j], dist)

            self.moveBestFirefly(fireflies, best_firefly_index, fnc)
            best_firefly_index = self.getBestFireflyIndex(fireflies, fnc)
            self.draw.append(copy.deepcopy(fireflies))
            t += 1
        return self.draw

    def getBestFireflyIndex(self, population, fnc):
        best = 0
        bestEval = fnc(population[best],True)
        for i in range(len(population)):
            tryBest = fnc(population[i],True)
            if bestEval > tryBest:
                bestEval = tryBest
                best = i
        return best

    def getEucleidianDistance(self, firefly1, firefly2):
        partialSum = 0
        for i in range(self.dimension):
            partialSum += (firefly1[i]-firefly2[i])**2
        return np.sqrt(partialSum)

    def moveFireflyThisTowards(self,thisFirefly, towardsFirefly, r):
        beta = 1**np.e**(-self.gamma*r**2)
        for i in range(self.dimension):
            rnNormal = np.random.normal(0, 1)
            thisFirefly[i] = thisFirefly[i] + beta*(towardsFirefly[i] - thisFirefly[i]) + self.alpha*rnNormal
        self.checkBoundaries(thisFirefly)
        return thisFirefly

    def generateSwarm(self):
        swarm = []
        for i in range(self.NP):
            x=np.random.uniform(self.lB,self.uB)
            y=np.random.uniform(self.lB,self.uB)
            swarm.append([x,y])
        return swarm

    def checkBoundaries(self, firefly):
        for i in range(self.dimension):
            if(firefly[i] > self.uB):
                firefly[i] = self.uB
            if(firefly[i] < self.lB):
                firefly[i] = self.lB

    def moveBestFirefly(self, population, best_firefly_index, fnc):
        copyofbest = copy.deepcopy(population[best_firefly_index])
        rnNormal = np.random.normal(0, 1)

        for i in range(self.dimension):
            copyofbest[i] += copyofbest[i] + + self.alpha*rnNormal
        if (fnc(population[i],True) > fnc(copyofbest,True)):
            population[i] = copyofbest
        self.checkBoundaries(population[i])




