# Source: https://medium.com/p/e396e98d8bf3 (for understanding genetic algorithm and using the base implementation)
import sys

import numpy as np

from src.Controller.Raking import Raking
import random

from src.Model.Way import Way


class Population:

    def __init__(self, row_val: int, col_val: int, garden_matrix: list, population):
        self.size = 100
        self.row_val = row_val
        self.col_val = col_val
        self.garden_matrix = garden_matrix
        self.population = population
        self.generation_count = 0
        self.best_fitness = 0

    def initializePopulation(self) -> list:
        self.population = [Raking(self.row_val, self.col_val, self.garden_matrix, Way(self.row_val, self.col_val)) for _ in range(self.size)]

    def evaluatePopulation(self):
        for individual in self.population:
            individual.work()
            if individual.solution:
                self.best_fitness = individual.fitness
        self.getFirstBestFitness()

    def isGO(self, x) -> bool:
        return x.game_over

    def filterGO(self):
        self.population = [individual for individual in self.population if not self.isGO(individual)]

    def isSolution(self, x) -> bool:
        return x.solution

    def findSolution(self) -> bool:
        for individual in self.population:
            if self.isSolution(individual):
                individual.printMatrix()
                return True

    def getFirstBestFitness(self) -> (int, int):
        self.population = sorted(self.population, key=lambda individual: individual.fitness, reverse=True)
        if len(self.population) >= 2:
            first_best_fitness = self.population[0].fitness
            self.best_fitness = first_best_fitness
        else:
            return

    def getFirstAndSecondBestFitness(self) -> (int, int):
        if len(self.population) >= 2:
            first_best_fitness = self.population[0].fitness
            self.best_fitness = first_best_fitness
            second_best_fitness = self.population[1].fitness
            return first_best_fitness, second_best_fitness
        else:
            return -1, -1

    def tournament(self, tour_participants_size: int, num_selections: int) -> list:
        selected_individuals = []

        for _ in range(num_selections):
            tournament = random.sample(self.population, tour_participants_size)
            tournament_winner = max(tournament, key=lambda individual: individual.fitness)
            selected_individuals.append(tournament_winner)

        return selected_individuals

    def oneToOneCrossover(self, parent_one, parent_two):

        garden_one = parent_one.garden_matrix
        garden_two = parent_two.garden_matrix

        # if one of the parents doesn't have a chromosome return parent not a new child
        if len(garden_one) <= 1 or len(garden_two) <= 1:
            return parent_one, parent_two

        # random crossover point
        crossover_point = random.randint(1, len(garden_one) - 1)
        child_one = garden_one[:crossover_point] + garden_two[crossover_point:]
        child_two = garden_two[:crossover_point] + garden_one[crossover_point:]

        # Create new children with new gardens
        new_child_one = Raking(self.row_val, self.col_val, child_one, Way(self.row_val, self.col_val))
        new_child_two = Raking(self.row_val, self.col_val, child_two, Way(self.row_val, self.col_val))

        return new_child_one, new_child_two

    def isChance(self, chance: int, mutation_probability: int) -> bool:
        return chance <= mutation_probability

    def generatePercentage(self) -> int:
        return random.randint(1, 100)

    def mutate_individual(self, individual, mutation_probability: int):
        for gen in individual.way.gen_list:
            chance = self.generatePercentage()
            if self.isChance(chance, mutation_probability):
                gen.mutate(mutation_probability, self.row_val, self.col_val)

        return individual

    def mutation(self, new_population: list):
        mutation_probability = 5
        for i in range(len(new_population)):
            chance = self.generatePercentage()
            if self.isChance(chance, mutation_probability):
                # mutated individual
                new_population[i] = self.mutate_individual(new_population[i], mutation_probability)

    def evolution(self) -> list:
        # rm game_over individuals
        self.filterGO()

        # elitism
        rm_worst_fitness = 4
        self.population = sorted(self.population, key=lambda individual: individual.fitness, reverse=True)
        self.population = self.population[:rm_worst_fitness]

        # list of new population
        new_population = []


        # tournament
        tour_participants_size = 3
        num_selections = 10
        tournaments_individuals = self.tournament(tour_participants_size, num_selections)

        # crossover
        for i in range(0, num_selections, 2):
            if i + 1 < num_selections:
                child1, child2 = self.oneToOneCrossover(tournaments_individuals[i], tournaments_individuals[i + 1])
                new_population.extend([child1, child2])

        # mutation
        self.mutation(new_population)

        # get the best fitness and add them to new_ population
        first_best_fitness, second_best_fitness = self.getFirstAndSecondBestFitness()
        if first_best_fitness != -1 and second_best_fitness != -1:
            best_individuals = [individual for individual in self.population if
                                individual.fitness in [first_best_fitness, second_best_fitness]]
            new_population.extend(best_individuals)

        return new_population
