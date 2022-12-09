
from tkinter import Y
from unittest.main import MAIN_EXAMPLES
import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from time import sleep
import math
import random


class Function:
    X=[]
    Y=[]
    Xm=[]
    Ym=[]
    Z=[]
class AckleyFunction(Function):
    def __init__(self):
        f=lambda x,y:-20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2)))-np.exp(0.5 * (np.cos(2 * np.pi * x)+np.cos(2 * np.pi * y))) + np.e + 20
        r_min, r_max = -32.768, 32.768
        xaxis = np.arange(r_min, r_max, 2.0)
        yaxis = np.arange(r_min, r_max, 2.0)
        self.X=xaxis
        self.Y=yaxis
        self.Xm, self.Ym = np.meshgrid(xaxis, yaxis)
        self.Z=f(self.Xm,self.Ym)

class ZakharovFunction(Function):
    def zakharov(self,x1,y):
        a= 0.5*x1+y
        b= x1*x1 +y*y +pow(a,2) +pow(a,4)
        return b
    def __init__(self):
        self.X = np.arange(-5, 10, 0.5)
        self.Y = np.arange(-5, 10, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = self.zakharov(self.Xm,self.Ym)

class MichalewiczFunction(Function):
    def __init__(self):
        f=lambda x,y: -1 * ( (np.sin(x) * np.sin((1 * x**2) / np.pi)**20) + (np.sin(y) * np.sin((2 * y**2) / np.pi)**20) )
        self.X = np.arange(0, np.pi, 0.5)
        self.Y = np.arange(0, np.pi, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z=f(self.Xm,self.Ym)
class LevyFunction(Function):
    def __init__(self):
        f=lambda x,y: np.sin(3*np.pi*x)**2 + (x-1)**2*(1+np.sin(3*np.pi*y)*np.sin(3*np.pi*y))+ (y-1)*(y-1)*(1+np.sin(2*np.pi*y)*np.sin(2*np.pi*y))
        self.X = np.arange(-10, 10, 0.5)
        self.Y = np.arange(-10, 10, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z=f(self.Xm,self.Ym)
class GriewankFunction(Function):
    def __init__(self):
        f=lambda x,y: (x**2+y**2)/4000 -np.cos(x/np.sqrt(2))*np.cos(y/np.sqrt(3))+1
        self.X = np.arange(-600, 600, 0.5)
        self.Y = np.arange(-600, 600, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z=f(self.Xm,self.Ym)

class RastriginFunction(Function):
    def __init__(self):
        f=lambda x,y: 10 + x**2 - 10* np.cos(2 * np.pi * x)  +(y**2 - 10 * np.cos(2 * np.pi * y))
        self.X = np.arange(-5.12, 5.12, 0.5) 
        self.Y = np.arange(-5.12, 5.12, 0.5) 
        
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = f(self.Xm, self.Ym)
       
    
class RosenbrockFunction(Function):
    def __init__(self):
        self.X = np.arange(-5, 10, 0.5)
        self.Y = np.arange(-5, 10, 0.5)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        f = lambda x,y: 100*((x-1)**2 )+ (y-x**2)**2
        self.Z = f(self.Xm,self.Ym)
        
class SchwefelFunction(Function):
    def __init__(self):
        xaxis = np.arange(-500, 500, 0.5)
        yaxis = np.arange(-500, 500, 0.5)
        x, y = np.meshgrid(xaxis, yaxis)
        self.X=xaxis
        self.Y=yaxis
        self.Xm=x
        self.Ym=y
        self.Z =self.fitnessFunc(x,y)
        
    def fitnessFunc(self,x,y):
        return (418.9829 * 2 - (x * (np.sin(np.sqrt(np.abs(x)))) + (y * np.sin(np.sqrt(np.abs(y))))))
class SphereFunction(Function):
    def __init__(self):
        self.X = np.arange(-5.12, 5.12, 0.25)
        self.Y = np.arange(-5.12, 5.12, 0.25)
        self.Xm, self.Ym = np.meshgrid(self.X, self.Y)
        self.Z = self.Xm**2 + self.Ym**2

class BlindSearcher:
    ngens=0
    g_minimum=999999999
    act_gen=0
    gens_rep=[]
    
    
    fnc=None
    def __init__(self,gens,fnc):
        self.ngens=gens
        self.fnc=fnc
        self.gens_min=[]
        for x in range(0,35):
            self.runGen(fnc)
    def runGen(self,fnc):
        rep=[]
        curent_min=999999999999
        cm_x=0
        cm_y=0
        cm_z=0
        for x in range(0,20):
            number = random.randint(0,fnc.Xm.shape[0]-1)
            numbery = random.randint(0,fnc.Ym.shape[0]-1)
            if(curent_min>fnc.Z[number][numbery]):
                curent_min=fnc.Z[number][numbery]
                cm_x=number
                cm_y=numbery
                cm_z=fnc.Z[number][numbery]
            if(self.g_minimum>fnc.Z[number][numbery]):
                self.g_minimum=fnc.Z[number][numbery]
            rep.append((number,numbery))

        self.gens_min.append((cm_x,cm_y,cm_z))
        self.gens_rep.append(rep)
            

class Declimber:
    X=[]
    Y=[]
    Z=[]
    actual_x=0
    actual_y=0
    actual_z=999999999999999
    fieldview=5
    vysledky=[]
    def __init__(self,func):
        self.vysledky=[]
        self.X=func.X
        self.Y=func.Y
        self.Z=func.Z
        self.actual_x=random.randint(0,len(self.X))
        self.actual_y=random.randint(0,len(self.Y))
        self.climb()
    def get_neighbor(self):
        number_x = int(np.random.normal(loc=self.actual_x, scale=self.X.shape[0] / 8, size=None))
        number_y = int(np.random.normal(loc=self.actual_y, scale=self.Y.shape[0] / 8, size=None))
        if number_x < 0:
            number_x = 0
        elif number_x >= self.X.shape[0]:
            number_x = self.X.shape[0] - 1
        if number_y < 0:
            number_y = 0
        elif number_y >= self.Y.shape[0]:
            number_y = self.Y.shape[0] - 1
        return (number_x, number_y)
    def evaluate(self,susedi):
        min_x=0
        min_y=0
        min_z=99999999999999
        for x in susedi:
            if min_z>self.Z[x[0]][x[1]]:
                min_z=self.Z[x[0]][x[1]]
                min_x=x[0]
                min_y=x[1]
        
        return (min_x,min_y)
    def climb(self):
        while(1):
            susedi=[]
            for i in range(0,100):
                susedi.append(self.get_neighbor())
            next=self.evaluate(susedi)
            self.actual_x=next[0]
            self.actual_y=next[1]
            if(self.actual_z<=self.Z[next[0]][next[1]]):
                break
            else:
                self.actual_z=self.Z[next[0]][next[1]]
                self.vysledky.append((next[0],next[1],self.actual_z))
            
    def run(self,fnc):
        self.jedu=True
        climb=None
        climb=Declimber(fnc)
        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', self.close_me)
        ax = plt.axes(projection='3d')
        ax.plot_surface(fnc.Xm,fnc.Ym,fnc.Z,alpha=0.2)
        plt.ion()
        while(self.jedu):
            
            amin=climb.vysledky[0][2]
            poi = None
            for vysl in climb.vysledky:
                    if(amin>=fnc.Z[vysl[0]][vysl[1]]):
                        amin=fnc.Z[vysl[0]][vysl[1]]
                        if (poi):
                            poi.remove()
                        poi=ax.scatter(fnc.X[vysl[1]], fnc.Y[vysl[0]], fnc.Z[vysl[0]][vysl[1]], color="red",alpha=0.9, marker = 'o', s = 100)
                    #ax.plot_surface(fnc.X,fnc.Y,fnc.Z)
                    #plt.draw()
                    plt.pause(0.00001)
            if (poi):
                poi.remove()
                
        
        plt.show(block=True)

class Controller:
    jedu=False
    def __init__(self):
        print("start")
        # #funguje
        fnc=SphereFunction()
        self.run(fnc)

        # #funguje
        fnc=SchwefelFunction()
        self.run(fnc)

        fnc=RosenbrockFunction()
        self.run(fnc)

        #funguje
        fnc=RastriginFunction()
        print(fnc.X.shape)
        print(fnc.Y.shape)
        print(fnc.Z.shape)
        self.run(fnc)

        #funguje
        fnc=GriewankFunction()
        self.run(fnc)

        fnc=LevyFunction()
        print(fnc.X.shape)
        print(fnc.Y.shape)
        print(fnc.Z.shape)
        self.run(fnc)
        

        fnc=MichalewiczFunction()
        self.run(fnc)
        
        fnc=ZakharovFunction()
        self.run(fnc)
        #funguje
        fnc=AckleyFunction()
        self.run(fnc)
        print("end")
    def close_me(self,akce):
        self.jedu=0
    def run(self,fnc):
        self.jedu=1
        bs=BlindSearcher(100,fnc)
        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', self.close_me)
        ax = plt.axes(projection='3d')
        ax.plot_surface(fnc.Xm,fnc.Ym,fnc.Z,alpha=0.2)
        plt.ion()
        while(self.jedu):
            
            amin=bs.gens_min[0][2]
            poi = None
            for gen in bs.gens_min:
                    if(amin>=gen[2]):
                        amin=gen[2]
                        if (poi):
                            poi.remove()
                        poi=ax.scatter(fnc.Xm[gen[1]][gen[1]], fnc.Ym[gen[0]][gen[0]], gen[2], color="red",alpha=0.9, marker = 'o', s = 100)
                    #ax.plot_surface(fnc.X,fnc.Y,fnc.Z)
                    #plt.draw()
                    plt.pause(0.00001)
            poi.remove()
                
        
        plt.show(block=True)
    

if __name__ == "__main__":
    ct=ClimbController()