# Source: https://medium.com/p/e396e98d8bf3 (for understanding genetic algorithm and using the base implementation)
import sys

from src.Controller.Raking import Raking
import random


class Population:

    # size random from 30 to 100
    def __init__(self, row_val: int, col_val: int, garden_matrix: list):
        self.size = 40
        self.row_val = row_val
        self.col_val = col_val
        self.population = self.initializePopulation()
        self.generation_count = 0
        self.best_fitness = 0
        self.garden_matrix = garden_matrix

    def initializePopulation(self) -> list:
        return [Raking(self.row_val, self.col_val, self.garden_matrix) for _ in range(self.size)]

    def isGO(self, x) -> bool:
        return x.game_over

    def filterGO(self):
        self.population = [individual for individual in self.population if not self.isGO(individual)]

    def getFirstAndSecondBestFitness(self) -> (int, int):
        if len(self.population) >= 2:
            first_best_fitness = self.population[0].fitness
            second_best_fitness = self.population[1].fitness
        return first_best_fitness, second_best_fitness

    def tournament(self, tour_participants_size: int, num_selections: int) -> list:
        selected_individuals = []

        for _ in range(num_selections):
            tournament = random.sample(self.population, tour_participants_size)
            tournament_winner = max(tournament, key=lambda individual: individual.fitness)
            selected_individuals.append(tournament_winner)

        return selected_individuals

    def oneToOneCrossover(self, parent_one, parent_two):
        crossover_point = random.randint(1, len(parent_one) - 1)

        child_one = parent_one.crossover_with(parent_two)
        child_two = parent_two.crossover_with(parent_one)
        child1_way = parent1.way[:crossover_point] + parent2.way[crossover_point:]
        child2_way = parent2.way[:crossover_point] + parent1.way[crossover_point:]

        return child_one, child_two



    # START
    # Generate the initial population
    # Compute fitness
    # REPEAT
    #       Selection
    #       Crossover
    #       Compute fitness
    # UNTIL I have solution or run through a lot of gens
    # STOP

    def evolution(self):
        # rm game_over individuals
        self.filterGO()

        # elitism
        rm_worst_fitness = 4
        self.population = sorted(self.population, key=lambda individual: individual.fitness, reverse=True)
        self.population = self.population[:rm_worst_fitness]

        # get best fitness
        first_best_fitness, second_best_fitness = self.getFirstAndSecondBestFitness()

        # tournament
        tour_participants_size = 3
        num_selections = 10
        tournaments_individuals = self.tournament(tour_participants_size, num_selections)

        # crossover
            # Divide individuals into two groups: one-to-one and random
        one_to_one_group = tournaments_individuals[:num_selections // 2]
        random_group = tournaments_individuals[num_selections // 2:]

        for i in range(0, one_to_one_group, 2):
            if i + 1 < one_to_one_group:
                child1, child2 = self.oneToOneCrossover(tournaments_individuals[i], tournaments_individuals[i + 1])
                new_population.extend([child1, child2])

        self.oneToOneCrossover(tournaments_individuals)


        # najlepsie dve nechavam, nic s nimi nerobim idu dalej
        # zvysnich 24 dat do 12 parov a krizit
        # alebo spravit 12 turnajov a spravit 4 deti vitazov
        # mutacie --> mutation(20 deti) --> return 6 zmutovanych deti --> nahodne vybera, ktore chromozomy mutuju, nahodne vyberiem ako mutuju (sanca 4% percent)


        pass

    # def getFirstFittest(self) -> Way:
    #     max_fit = sys.maxint
    #     max_fit_idx = 0
    #
    #     for idx, road in enumerate(self.ways):
    #         if max_fit <= road.fitness:
    #             max_fit = road.fitness
    #             max_fit_idx = idx
    #
    #     self.best_fitness = self.ways[max_fit_idx].fitness
    #     return self.ways[max_fit_idx]
    #
    #
    # def getSecondFittest(self) -> Way:
    #     max_first_fit = 0
    #     max_second_fit = 0
    #
    #     for idx, road in enumerate(self.ways):
    #         if road.fitness > self.ways[max_first_fit].fitness:
    #             max_second_fit = max_first_fit
    #             max_first_fit = idx
    #         elif road.fitness > self.ways[max_second_fit].fitness:
    #             max_second_fit = idx
    #
    #     return self.ways[max_second_fit]
    #
    #
    # def getFragileFittestIdx(self) -> int:
    #     min_fit = sys.maxsize
    #     min_fit_idx = 0
    #
    #     for idx, way in enumerate(self.ways):
    #         if min_fit >= way.fitness:
    #             min_fit = way.fitness
    #             min_fit_idx = 0
    #
    #     return min_fit_idx

    # def getFitness(self):
    #     for way in self.ways:
    #         way.calculateFitness()
    #
    #     getBestFitness()
