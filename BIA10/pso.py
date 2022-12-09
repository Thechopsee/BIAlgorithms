
import copy
from time import sleep
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction

class PSOSolution:
    def __init__(self,lower_bound, upper_bound, number_of_individuals, number_of_gen_cycles,dimensions):
        self.dimensions= dimensions
        self.draw_swarm = []
        self.lB = lower_bound  
        self.uB = upper_bound
        self.NP = number_of_individuals
        self.M_max = number_of_gen_cycles
        self.c1 = 1
        self.c2 = 2
        self.v_mini = (upper_bound-lower_bound)/80
        self.v_maxi = self.v_mini*3
        self.f = np.inf
        self.bestofbest=None

    def generateSwarm(self):
        susedi = []
        for x in range(self.NP):
            pi = []
            for y in range(self.dimensions):
                pi.append(np.random.uniform(self.lB,self.uB))
            susedi.append(pi)
        return susedi
    def findBest(self, swarm, function):
        personalBest = function(swarm[0],True)
        personalBestIndex = 0
        count=0
        for particle in swarm:
            value = function(particle,True)
            if(personalBest > value):
                personalBestIndex = count
                personalBest = value
            count+=1
        self.bestofbest=personalBest
        return swarm[personalBestIndex]
    def particle_swarm(self, fnc):
        
        swarm = self.generateSwarm() 
        gBest = self.findBest(swarm, fnc) 
        
        pBest = copy.deepcopy(swarm)
        velocity = []
        for i in range(self.NP):
            pi = []
            for j in range(self.dimensions):
                pi.append(np.random.uniform(self.v_mini, self.v_maxi))
            velocity.append(pi)
        m = 0
        
        while m < self.M_max:
            for i in range(len(swarm)):
                velocity[i] = self.recalculateParticleVelocity(velocity[i], swarm[i], pBest[i], gBest, m)
                swarm[i] = self.boundaries(np.add(swarm[i], velocity[i]))
                
                fnc1=fnc(swarm[i],True)
                if(fnc1 < fnc(pBest[i],True)):
                    pBest[i] = copy.deepcopy(swarm[i])
                if(fnc1 < fnc(gBest,True)):
                        gBest = copy.deepcopy(pBest[i])
                        self.bestofbest=fnc1
                        
            self.draw_swarm.append(copy.deepcopy(swarm))
            m += 1
        

    def recalculateParticleVelocity(self, velocity, particle, pBest, gBest, i):
        ws = 0.9
        we = 0.4
        r1 = np.random.uniform()
        r2 = np.random.uniform()
        w = ws * ((ws-we)*i+1)/self.M_max
        newVelocity = np.add(np.add(np.multiply(velocity, w), np.multiply((r1 * self.c1), (np.subtract(pBest, particle)))), np.multiply((r2 * self.c2), (np.subtract(gBest, particle))))
        newVelocity=self.fixBoundaries(newVelocity)
        return newVelocity

    def fixBoundaries(self, velocity):
        for i in range(len(velocity)):
            if(abs(velocity[i]) < self.v_mini):
                if(velocity[i]<0):
                    velocity[i]=-self.v_mini
                else:
                    velocity[i]=self.v_mini    
            elif(abs(velocity[i]) > self.v_maxi):
                if(velocity[i]<0):
                    velocity[i] = -self.v_maxi
                else:
                    velocity[i] = self.v_maxi
        return velocity

    def boundaries(self,vector):
            for i in range(len(vector)):
                if(vector[i] > self.uB):
                    vector[i] = self.uB
                elif (vector[i] < self.lB):
                    vector[i] = self.lB
            return vector

