# Source: https://medium.com/p/e396e98d8bf3 (for understanding genetic algorithm and using the base implementation)
import sys

from src.Model import Way


class Population:
    def __init__(self, ways: Way):
        self.best_fitness = 0
        self.ways = ways

    # int pop_size = 10
    # Road[] roads = new Road[10]


    def initializePopulation(self):
        for way in self.way:
            way = Way()


    def getFirstFittest(self) -> Way:
        max_fit = sys.maxint
        max_fit_idx = 0

        for idx, road in enumerate(self.ways):
            if max_fit <= road.fitness:
                max_fit = road.fitness
                max_fit_idx = idx

        self.best_fitness = self.ways[max_fit_idx].fitness
        return self.ways[max_fit_idx]


    def getSecondFittest(self) -> Way:
        max_first_fit = 0
        max_second_fit = 0

        for idx, road in enumerate(self.ways):
            if road.fitness > self.ways[max_first_fit].fitness:
                max_second_fit = max_first_fit
                max_first_fit = idx
            elif road.fitness > self.ways[max_second_fit].fitness:
                max_second_fit = idx

        return self.ways[max_second_fit]


    def getFragileFittestIdx(self) -> int:
        min_fit = sys.maxsize
        min_fit_idx = 0

        for idx, way in enumerate(self.ways):
            if min_fit >= way.fitness:
                min_fit = way.fitness
                min_fit_idx = 0

        return min_fit_idx


    def getFitness(self):
        for way in self.ways:
            way.calculateFitness()

        getBestFitness()



