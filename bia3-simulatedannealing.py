from hashlib import new
from tkinter import Y
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from time import sleep
import math
import random
from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction


class SAController:
    jedu=False
    def close_me(self,akce):
        self.jedu=False
    def __init__(self):
        sp=SphereFunction()
        
        
        self.run(sp)

        sp=SchwefelFunction()
        self.run(sp)

        sp=RosenbrockFunction()
        self.run(sp)

        sp=RastriginFunction()
        self.run(sp)

        sp=GriewankFunction()
        self.run(sp)

        sp=LevyFunction()
        self.run(sp)

        sp=MichalewiczFunction()
        self.run(sp)

        sp=ZakharovFunction()
        self.run(sp)

        sp=AckleyFunction()
        self.run(sp)
    def run(self,fnc):
        self.jedu=True
        fig = plt.figure()
        number_x = int(np.random.normal(loc=0, scale=fnc.X.shape[0]/2, size=None))
        number_y = int(np.random.normal(loc=0, scale=fnc.Y.shape[0]/2 , size=None))
        sa=SimulatedAnnealing(fnc,(number_x,number_y,fnc.Z[number_x][number_y]),100,0.5)
        sa.run()
        gen=sa.generations
        ax = plt.axes(projection='3d')
        fig.canvas.mpl_connect('close_event', self.close_me)
        ax.plot_surface(fnc.Xm,fnc.Ym,fnc.Z,alpha=0.2)
        plt.ion()
        while(self.jedu):
            poi = None
            for vysl in gen:
                if (poi):
                    poi.remove()
                poi=ax.scatter(fnc.X[vysl[1]], fnc.Y[vysl[0]], fnc.Z[vysl[0]][vysl[1]], color="red",alpha=0.9, marker = 'o', s = 100)
                plt.pause(0.00001)
            if (poi):
                poi.remove()
        plt.show(block=True)


class SimulatedAnnealing:
    generations=[]
    def __init__(self,fnc, initialSolution, initialTemp, finalTemp, iterationPerTemp=2, alpha=0.95):
        self.solution = initialSolution
        self.fnc=fnc
        self.currTemp = initialTemp
        self.finalTemp = finalTemp
        self.iterationPerTemp = iterationPerTemp
        self.alpha = alpha
        self.decrementRule = self.linearTempReduction
        self.generations=[]
    def neighborOperator(self):
        sused=[]
        for x in range(0,self.iterationPerTemp):
            number_x = int(np.random.normal(loc=self.solution[0], scale=self.fnc.X.shape[0] / 12, size=None))
            number_y = int(np.random.normal(loc=self.solution[1], scale=self.fnc.Y.shape[0] / 12, size=None))
            if number_x < 0:
                number_x = 0
            elif number_x >= self.fnc.X.shape[0]:
                number_x = self.fnc.X.shape[0] - 1
            if number_y < 0:
                number_y = 0
            elif number_y >= self.fnc.Y.shape[0]:
                number_y = self.fnc.Y.shape[0] - 1
            sused.append((number_x,number_y,self.fnc.Z[number_x][number_y]))

        return sused
    def linearTempReduction(self):
        self.currTemp *= self.alpha
    def isTerminationCriteriaMet(self): 
        return self.currTemp <= self.finalTemp
    def run(self):
        while not self.isTerminationCriteriaMet():
                neighbors = self.neighborOperator()
                rcn= random.randint(1,len(neighbors)-1)
                newSolution = neighbors[rcn]  
                cost=self.solution[2]-newSolution[2]
                if(cost>=0):
                    self.solution=newSolution
                    self.generations.append(newSolution)
                elif np.random.uniform() < np.e**(-(newSolution[2]-self.solution[2]) / self.currTemp):
                        print(self.currTemp)
                        self.solution = newSolution
                        self.generations.append(newSolution)
                self.decrementRule()

if __name__ == "__main__":
    ct=SAController()