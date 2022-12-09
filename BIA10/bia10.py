from de import DeSolution
from pso import PSOSolution
from soma import SOMASolution
from firefly import FASolution
from TLBO import TLBO
import numpy as np
from BIAfunctions import SphereFunction,SchwefelFunction,RosenbrockFunction,RastriginFunction,GriewankFunction,LevyFunction,MichalewiczFunction,ZakharovFunction,AckleyFunction
class Driver:
    numExp=30
    numDim=30
    numP=35
    numgen=30
    def driverFA(self):
        print("SphereFunction")
        self.runFA(SphereFunction())
        print("SchwefelFunction")
        self.runFA(SchwefelFunction())
        print("RosenbrockFunction")
        self.runFA(RosenbrockFunction())
        print("RastriginFunction")
        self.runFA(RastriginFunction())
        print("GriewankFunction")
        self.runFA(GriewankFunction())
        print("LevyFunction")
        self.runFA(LevyFunction())
        print("MichalewiczFunction")
        self.runFA(MichalewiczFunction())
        print("ZakharovFunction")
        self.runFA(ZakharovFunction())
        print("AckleyFunction")
        self.runFA(AckleyFunction())
    def runFA(self,sf):
         for x in range(self.numExp):
            sf.reset()
            solution = FASolution(sf.lb,sf.ub,self.numP,self.numgen,self.numDim)
            try:
                    vysl=solution.firefly(sf.useFn)
                    personalBest=None
                    for i,particle in enumerate(vysl):
                        if(personalBest > sf.useFn(particle,False)):
                            personalBest = sf.useFn(particle,False)
                    print(personalBest)
            except:
                vysl=solution.draw[len(solution.draw)-1]
                personalBest=99999999999999999999999999
                for i,particle in enumerate(vysl):
                        if(personalBest > sf.useFn(particle,False)):
                            personalBest = sf.useFn(particle,False)
                print(personalBest)
    def driverSOMA(self):
        print("SphereFunction")
        self.runSOMA(SphereFunction())
        print("SchwefelFunction")
        self.runSOMA(SchwefelFunction())
        print("RosenbrockFunction")
        self.runSOMA(RosenbrockFunction())
        print("RastriginFunction")
        self.runSOMA(RastriginFunction())
        print("GriewankFunction")
        self.runSOMA(GriewankFunction())
        print("LevyFunction")
        self.runSOMA(LevyFunction())
        print("MichalewiczFunction")
        self.runSOMA(MichalewiczFunction())
        print("ZakharovFunction")
        self.runSOMA(ZakharovFunction())
        print("AckleyFunction")
        self.runSOMA(AckleyFunction())
    def runSOMA(self,sf):
        for x in range(self.numExp):
            sf.reset()
            solution = SOMASolution(sf.lb,sf.ub,self.numP,self.numgen,self.numDim)
            try:
                    vysl=solution.soma(sf.useFn)
                    personalBest=None
                    for i,particle in enumerate(vysl):
                        if(personalBest > sf.useFn(particle,False)):
                            personalBest = sf.useFn(particle,False)
                    print(personalBest)
            except:
                vysl=solution.draw[len(solution.draw)-1]
                personalBest=99999999999999999999999999
                for i,particle in enumerate(vysl):
                        if(personalBest > sf.useFn(particle,False)):
                            personalBest = sf.useFn(particle,False)
                print(personalBest)
    def driverDE(self):
        print("SphereFunction")
        self.runDE(SphereFunction())
        print("SchwefelFunction")
        self.runDE(SchwefelFunction())
        print("RosenbrockFunction")
        self.runDE(RosenbrockFunction())
        print("RastriginFunction")
        self.runDE(RastriginFunction())
        print("GriewankFunction")
        self.runDE(GriewankFunction())
        print("LevyFunction")
        self.runDE(LevyFunction())
        print("MichalewiczFunction")
        self.runDE(MichalewiczFunction())
        print("ZakharovFunction")
        self.runDE(ZakharovFunction())
        print("AckleyFunction")
        self.runDE(AckleyFunction())
    def runDE(self,sf):
        for x in range(self.numExp):
            sf.reset()
            pole=[]
            solution = DeSolution(sf.lb,sf.ub,self.numP,self.numgen,self.numDim)
            try:
                    vysl=solution.differentialEvolution(sf)
                    for x in vysl:
                        pole.append(sf.useFn(x,False))
                    print(np.min(pole))
            except ValueError:
                vysl=solution.draw_evolution[-1] 
                for x in vysl:
                        pole.append(sf.useFn(x,False))
                print(np.min(pole))
    def driverPSO(self):
        print("SphereFunction")
        self.runPSO(SphereFunction())
        print("SchwefelFunction")
        self.runPSO(SchwefelFunction())
        print("RosenbrockFunction")
        self.runPSO(RosenbrockFunction())
        print("RastriginFunction")
        self.runPSO(RastriginFunction())
        print("GriewankFunction")
        self.runPSO(GriewankFunction())
        print("LevyFunction")
        self.runPSO(LevyFunction())
        print("MichalewiczFunction")
        self.runPSO(MichalewiczFunction())
        print("ZakharovFunction")
        self.runPSO(ZakharovFunction())
        print("AckleyFunction")
        self.runPSO(AckleyFunction())
    def runPSO(self,sf):
        for x in range(self.numExp):
            sf.reset()
            solution = PSOSolution(sf.lb,sf.ub,self.numP,self.numgen,self.numDim)
            try:
                    vysl=solution.particle_swarm(sf.useFn)
                    print(solution.bestofbest)
            except:
                print(solution.bestofbest)
    def driverTLBO(self):
        print("SphereFunction")
        self.runTLBO(SphereFunction())
        print("SchwefelFunction")
        self.runTLBO(SchwefelFunction())
        print("RosenbrockFunction")
        self.runTLBO(RosenbrockFunction())
        print("RastriginFunction")
        self.runTLBO(RastriginFunction())
        print("GriewankFunction")
        self.runTLBO(GriewankFunction())
        print("LevyFunction")
        self.runTLBO(LevyFunction())
        print("MichalewiczFunction")
        self.runTLBO(MichalewiczFunction())
        print("ZakharovFunction")
        self.runTLBO(ZakharovFunction())
        print("AckleyFunction")
        self.runTLBO(AckleyFunction())
    def runTLBO(self,sf):
        for x in range(self.numExp):
            sf.reset()
            solution = TLBO(NP = self.numP, lb = sf.lb, ub = sf.ub, iterations = self.numgen, plotEnabled = True,dimensions=self.numDim,f=sf.useFn)
            try:
                    vysl=solution.runTLBO()
                    print(sf.useFn(solution.findBest(),False))
            except ValueError as e:
                sf.reset()
                print(sf.useFn(solution.findBest(),False))
    def __init__(self):
        self.driverDE() 
        #self.driverPSO()
        #self.driverSOMA()
        #self.driverFA()
        #self.driverTLBO()
        

Driver()