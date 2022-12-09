
from logging import critical
from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
import math
import random 
import copy
from Renderer import Render

starting_city=0
num_city=20
class City:
    pos_x=0
    pos_y=0
    id=0
    def __init__(self,x,y,id):
        self.pos_x=x
        self.pos_y=y
        self.id=id
    def __str__(self):
        return "("+str(self.pos_x)+","+str(self.pos_y)+","+str(self.id)+")"

class Path:
        cities=[]
        distances=[]
        route=0
        def __init__(self,cities,distances):
            self.cities=cities
            self.distances=distances
        def __str__(self) -> str:
            for x in self.cities:
                print(str(x))
            return "\n"
        def mutate(self):
            r1=random.randint(1,len(self.cities)-2)
            r2=random.randint(1,len(self.cities)-2)
            x=copy.deepcopy(self.cities[r1])
            y=copy.deepcopy(self.cities[r2])
            self.cities[r1]=y
            self.cities[r2]=x
        def checkSmicka(self,tsp):
            misingid=[]
            for x in range(0,len(self.cities)-1):
                misingid.append(0)
            for y in self.cities:
                misingid[y.id]+=1
            misingid.pop(0)
            cnt=1
            for x in misingid:
                if(x>1):
                        count=1
                        for y in misingid:
                            if(y==0):
                                y+=1
                                x-=1
                                misingid[count-1]=y
                                misingid[cnt-1]=x
                                ctz=0
                                for z in self.cities:
                                    if (z.id==cnt):
                                        self.cities[ctz]=tsp[count]
                                        break
                                    ctz+=1
                                break

                            count+=1
                cnt+=1
                
        def getHalf(self,h):
            if(h==0):
                tempc=self.cities[:len(self.cities)//2]
                return tempc
            else:
                tempc=self.cities[len(self.cities)//2:]
                return tempc
        def evaluateMyself(self):
            dist=0.0
            for x in range(0,len(self.cities)-1):
                dist+=self.distances[self.cities[x].id+self.cities[x+1].id*(len(self.cities)-1)]
            self.route=dist
        def printDistanceM(self):
            for i in range(0,len(self.cities)-1):
                line=""
                for j in range(0,len(self.cities)-1):
                    line+=str("{:10.4f}".format(self.distances[j+i*(len(self.cities)-1)]))
                    line+=" "
                print(line)
             
class TSP:
    cities=[]
    distMatrix=[]
    paths=[]
    best_paths=[]
    crnt_min_id=0
    def __init__(self):
        
        self.generateCities()
        self.generateDistanceMatrix()
        for x in range(0,20):
            self.paths.append(self.generatePath())
    def generateDistanceMatrix(self):
        for c in self.cities:
            for c2 in self.cities:
                dist = math.sqrt((c.pos_x-c2.pos_x)**2 + (c.pos_y-c2.pos_y)**2)
                self.distMatrix.append(dist)
    def generateCities(self):
        for i in range(0,num_city):
            number_x = np.random.randint(250)
            number_y = np.random.randint(250)
            self.cities.append(City(number_x,number_y,i))
        
    def generatePath(self):
        cities=copy.copy(self.cities)
        cities.remove(cities[starting_city])
        random.shuffle(cities)
        cities.insert(0, self.cities[starting_city])
        cities.append(self.cities[starting_city])
        path=Path(cities,self.distMatrix)
        return path
    def mnoz(self,parent1,parent2):
        list1=[]
        list2=[]
        cross=np.random.randint(1,len(parent1.cities)-1)
        for x in range(0,cross):
            list1.append(parent1.cities[x])
        for y in range(cross,len(parent2.cities)):
            list2.append(parent2.cities[y])
        for x in list2:
                list1.append(x)
        tp=Path(list1,self.distMatrix)
        tp.checkSmicka(self.cities)
        return tp
    def runGenerace(self):
        min_id=0
        min_dist=999999999999999999
        count=0
        for x in self.paths:
            x.evaluateMyself()
            if(x.route<min_dist):
                min_dist=x.route
                min_id=count
                
            count+=1
        
        self.crnt_min_id=min_id
        if(len(self.best_paths)>0):
            if(min_dist<self.best_paths[len(self.best_paths)-1].route):
                self.best_paths.append(self.paths[min_id])
            else:
                self.best_paths.append(self.best_paths[len(self.best_paths)-1])
        else:
            self.best_paths.append(self.paths[min_id])
        new_gen=copy.deepcopy(self.paths)
        for j in range(0,len(self.paths)):
                r2=random.randint(0,len(self.paths)-1)
                if(r2==j):
                    r2=random.randint(0,len(self.paths)-1)
                tpt=self.mnoz(self.paths[j],self.paths[r2])
                if(np.random.uniform(0,1)<0.5):
                    tpt.mutate()
                tpt.evaluateMyself()
                if(tpt.route<self.paths[j].route):
                    new_gen[j]=tpt
        self.paths=new_gen
class TSPConroller:
    jedu=True
    def close_me(self,akce):
        self.jedu=False

    tsp=None
    num_gen=200
    def __init__(self) -> None:
        self.tsp=TSP()
            
    def runGenetic(self):
        for x in range(0,self.num_gen):
            self.tsp.runGenerace()
        

if __name__ == "__main__":
    rn=TSPConroller()
    rn.runGenetic()
    ren=Render()
    ren.show(rn.tsp.cities,rn.tsp.best_paths)
    # pt=rn.tsp.generatePath()
    # pt.printDistanceM()
    # pt.evaluateMyself()
    # print(pt)
    # print(pt.route)
    # pth1=pt.getHalf(0)
    # print("Before mutate")
    # for x in pth1:
    #     print(str(x))
    # pth2=pt.getHalf(1)
    # for x in pth2:
    #     print(str(x))
    # pt.mutate()
    # print("After mutate")
    # for x in pth1:
    #     print(str(x))
    # pth2=pt.getHalf(1)
    # for x in pth2:
    #     print(str(x))
    # pt2=rn.tsp.generatePath()
    # print("Parents")
    # print("parent1")
    # pt.printMe()
    # print("parent2")
    # pt2.printMe()
    # print("Child")
    # pt3=rn.tsp.mnoz(pt,pt2)
    # pt3.printMe()
