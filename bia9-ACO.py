from logging import critical
from turtle import distance
import numpy as np
import matplotlib.pyplot as plt
import math
import random
import copy

starting_city=0
num_city = 25

class City:
    pos_x = 0
    pos_y = 0
    id = 0

    def __init__(self, x, y, id):
        self.pos_x = x
        self.pos_y = y
        self.id = id

    def __str__(self):
        return "(" + str(self.pos_x) + "," + str(self.pos_y) + "," + str(self.id) + ")"
class Path:
    def __init__(self, city_order, edges,lenght):
        self.total_length=lenght
        self.city_order=city_order
        self.edges=edges

class TSP:
    cities = []
    distMatrix = []
    visibilityMatrix = []
    pheromoneMatrix = []
    paths = []
    best_paths = []
    best_result = None 
    crnt_min_id = 0
    q = 10
    evaporation_coefficient = 0.5
    pi = 1
    di = 2

    def __init__(self):
        self.generateCities()
        self.generateDistanceMatrix()
        self.generateVisibilityMatrix()
        self.pheromoneMatrix = np.empty((len(self.cities), len(self.cities)))
        self.pheromoneMatrix.fill(1)

    def generateDistanceMatrix(self):
        for c in self.cities:
            line=[]
            for c2 in self.cities:
                dist = math.sqrt((c.pos_x - c2.pos_x) ** 2 + (c.pos_y - c2.pos_y) ** 2)
                line.append(dist)
            self.distMatrix.append(line)
       

    def generateCities(self):
        for i in range(0, num_city):
            number_x = np.random.randint(250)
            number_y = np.random.randint(250)
            self.cities.append(City(number_x, number_y, i))

    def generateVisibilityMatrix(self):
        self.visibilityMatrix = np.empty((len(self.cities), len(self.cities)))
        for i in range(len(self.cities)):
            for j in range(len(self.cities)):
                if self.distMatrix[i][j] == 0:
                    if i == j:
                        self.visibilityMatrix[i][j] = 0
                    else:
                        self.visibilityMatrix[i][j] = 1
                    continue
                self.visibilityMatrix[i][j] = 1 / self.distMatrix[i][j]

    def runGenerace(self):
        cesty = []
        genBest = None
        for j in range(len(self.cities)):
            antResult = self.generateAntPath(self.cities[j])
            cesty.append(antResult)
            if genBest is None:
                genBest = antResult
            if antResult.total_length < genBest.total_length:
                genBest = antResult
        self.pheromoneMatrix = self.pheromoneMatrix * (1 - self.evaporation_coefficient)

        if(self.best_result is None):
            self.best_result = genBest
        else:
            if (genBest.total_length < self.best_result.total_length):
                self.best_result = genBest

        for cesta in cesty:
            delta = self.q/cesta.total_length
            for edge in cesta.edges:
                self.pheromoneMatrix[edge[0]][edge[1]] += delta
                for hranaVNejlepsiCeste in self.best_result.edges:  
                    if edge == hranaVNejlepsiCeste:                 
                        self.pheromoneMatrix[edge[0]][edge[1]] += delta/4 

        self.best_paths.append((self.best_result.city_order, self.best_result.total_length))

    def generateAntPath(self, starting_node):
        visited = np.empty(len(self.cities))
        visited.fill(1)
        visited[starting_node.id] = 0
        total_length = 0
        current_city = starting_node
        steps = 0
        order = [starting_node]
        edges = []

        while steps < len(self.cities) - 1:
            jumps_neighbors = []
            vysledky = []
            for city in self.cities:
                if visited[city.id] != 0:
                    pheromone_level = self.pheromoneMatrix[current_city.id][city.id]
                    vysledky.append(((pheromone_level ** self.pi) *(self.visibilityMatrix[current_city.id][city.id] ** self.di)))
                    jumps_neighbors.append(city)
            citatel = sum(vysledky) 
            for i in range(len(vysledky)):
                vysledky[i] = vysledky[i] / citatel

            next_step = random.choices(jumps_neighbors, weights=vysledky)[0]
            visited[next_step.id] = 0
            edges.append([current_city.id, next_step.id])
            current_city = next_step
            order.append(self.cities[next_step.id])

            steps += 1
        order.append(starting_node)
        edges.append([current_city.id, starting_node.id])
        total_length = self.evaluatePath(order)
        return Path(order,edges,total_length)


    def evaluatePath(self, cities_order):
        dist = 0.0
        for x in range(len(cities_order) - 1):
            dist += self.distMatrix[cities_order[x].id][cities_order[x + 1].id]
        return dist

class TSPConroller:
    jedu = True
    def close_me(self, akce):
        self.jedu = False
    tsp = None
    num_gen = 100
    def __init__(self) -> None:
        self.tsp = TSP()

    def show(self):
        fig = plt.figure()
        fig.canvas.mpl_connect('close_event', self.close_me)
        x = []
        y = []
        for z in self.tsp.cities:
            x.append(z.pos_x)
            y.append(z.pos_y)
        start_pos = []
        end_pos = []
        ax = plt.plot(x, y, 'ro')
        plt.ion()
        ptt = None
        pt = None
        while (self.jedu):
            ct = 0
            for i in self.tsp.best_paths:
                if (not self.jedu):
                    break
                if (pt):
                    start_pos = []
                    end_pos = []
                    pt.remove()
                for j in range(len(i[0])):
                    start_pos.append(i[0][j].pos_x)
                    end_pos.append(i[0][j].pos_y)

                print("gen" + str(ct) + ":" + str(i[1]))
                fig.suptitle("gen" + str(ct) + ":" + str(i[1]))
                pt, = plt.plot(start_pos, end_pos)

                plt.pause(0.001)
                ct += 1

    def runGenetic(self):
        for x in range(0, self.num_gen):
            self.tsp.runGenerace()


if __name__ == "__main__":
    rn = TSPConroller()
    rn.runGenetic()
    rn.show()