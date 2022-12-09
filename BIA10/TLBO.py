import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from typing import List
import copy
from Renderer import Render
from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction

class TLBO:
    def __init__(self, NP, lb, ub, iterations, plotEnabled,dimensions,f):
        self.NP = NP
        self.lb = lb
        self.ub = ub
        self.iterations = iterations
        self.plotEnabled = plotEnabled
        self.f=f
        self.dim = dimensions
        self.pop=[]
        self.draw=[]

    def initPop(self):
        susedi = []
        for x in range(self.NP):
            pi = []
            for y in range(self.dim):
                pi.append(np.random.uniform(self.lb,self.ub))
            susedi.append(pi)
        self.pop=susedi
        return susedi
    
    def findBestIndex(self):
        bestIndex = None
        bestFitness = float("inf")

        for i in range(self.NP):
            if self.f(self.pop[i],True) < bestFitness:
                bestIndex = i
                bestFitness = self.f(self.pop[i],True)

        return bestIndex

    def findMean(self):
        mean = self.pop[0]

        for i in range(1, self.NP):
            mean = np.add(mean,self.pop[i])
        mean = mean / self.NP
        return mean

    def teacherPhase(self):
        teacherIndex = self.findBestIndex()
        teacher = self.pop[teacherIndex]
        mean = self.findMean()

        for i in range(self.NP):
            if i == teacherIndex:
                continue

            randVector = [np.random.uniform() for i in range(self.dim)]
            teacherFactor = round(1 + np.random.uniform())

            positionNew = self.pop[i] + randVector * (teacher - teacherFactor * mean)
            self.boundaries(positionNew)
            if self.f(positionNew,True) < self.f(self.pop[i],True):
                self.pop[i] = positionNew
    def boundaries(self,vector):
            for i in range(len(vector)):
                if(vector[i] > self.ub):
                    vector[i] = self.ub
                elif (vector[i] < self.lb):
                    vector[i] = self.lb
            return vector

    def learnerPhase(self):
        popTmp = self.pop.copy()

        for i in range(self.NP):
            choice = np.random.choice(range(self.NP))
            while choice == i:
                choice = np.random.choice(range(self.NP))

            randVector = [np.random.uniform() for j in range(self.dim)]

            if self.f(self.pop[i],True) < self.f(popTmp[choice],True):
                positionNew = self.pop[i] + randVector * (np.subtract(self.pop[i],popTmp[choice]))
            
            else:
                positionNew = self.pop[i] + randVector * (np.subtract(popTmp[choice],self.pop[i]))

            self.boundaries(positionNew)
            if self.f(positionNew,True) < self.f(self.pop[i],True):
                self.pop[i]= positionNew
        

    def findBest(self):
        return self.pop[self.findBestIndex()]

    def iterate(self):
        for i in range(self.iterations):
            self.teacherPhase()
            self.learnerPhase()
            self.draw.append(copy.deepcopy(self.pop))

    def runTLBO(self):
        self.initPop()
        self.iterate()
        


# rn=Render()
# sf=SchwefelFunction()
# solution = TLBO(NP = 10, lb = sf.lb, ub = sf.ub, iterations = 10, plotEnabled = True,dimensions=2,f=sf.useFn)
# solution.runTLBO()
# rn.runanim(solution.draw,sf)

