
import copy
from time import sleep
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

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
        self.c1 = 1
        self.c2 = 2
        self.v_mini = (upper_bound-lower_bound)/80
        self.v_maxi = self.v_mini*3
        self.f = np.inf
       

    def generateSwarm(self):
        swarm = []
        for i in range(self.NP):
            x=np.random.uniform(self.lB,self.uB)
            y=np.random.uniform(self.lB,self.uB)
            swarm.append((x,y))
        return swarm
    def findBest(self, swarm, function):
        personalBest = function(swarm[0][0],swarm[0][1])
        personalBestIndex = 0
        count=0
        for particle in swarm:
            value = function(particle[0],particle[1])
            if(personalBest > value):
                personalBestIndex = count
                personalBest = value
            count+=1

        return swarm[personalBestIndex]
    def particle_swarm(self, fnc):
        swarm = self.generateSwarm() 
        gBest = self.findBest(swarm, fnc) 
        pBest = copy.deepcopy(swarm)
        velocity = []
        for i in range(self.NP):
            pi = []
            for j in range(self.dimension):
                pi.append(np.random.uniform(self.v_mini, self.v_maxi))
            velocity.append(pi)
        m = 0
        while m < self.M_max:
            for i in range(len(swarm)):
                velocity[i] = self.recalculateParticleVelocity(velocity[i], swarm[i], pBest[i], gBest, m)
                swarm[i] = self.boundaries(np.add(swarm[i], velocity[i]))
                if(fnc(swarm[i][0],swarm[i][1]) < fnc(pBest[i][0],pBest[i][1])):
                    pBest[i] = copy.deepcopy(swarm[i])
                if(fnc(swarm[i][0],swarm[i][1]) < fnc(gBest[0],gBest[1])):
                        gBest = copy.deepcopy(pBest[i])

            self.draw.append(copy.deepcopy(swarm))
            m += 1

    def recalculateParticleVelocity(self, velocity, particle, pBest, gBest, i):
        ws = 0.9
        we = 0.4
        r1 = np.random.uniform()
        r2 = np.random.uniform()
        #w = ws - ((ws-we)*i)/self.M_max
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




sf=SphereFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=SchwefelFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=RosenbrockFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=RastriginFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=GriewankFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=LevyFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=MichalewiczFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=ZakharovFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)

sf=AckleyFunction()          
solution = Solution(sf.lb,sf.ub,15,50)
solution.particle_swarm(sf.useF)
r=Render()
r.runanim(solution.draw,sf)


