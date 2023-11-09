import time

from src.Controller.Raking import Raking
from src.Model.Population import Population
from src.View.Input import Input

def findBestFitness(population: Population) -> int:
    return population.best_fitness
def printGeneration(counter: int, population: Population):
        print(f'generation: {counter} best fitness: {findBestFitness(population)}')

def main():
    # get input from the file
    input = Input()
    row_num, col_num, garden_matrix = input.openAndProccessFile()

    generation_limit = 500
    generation_counter = 1

    # initialize population
    population = Population(row_num, col_num, garden_matrix, None)
    start_time = time.time()
    population.initializePopulation()
    population.evaluatePopulation()
    printGeneration(generation_counter, population)

    while generation_limit > generation_counter:

        if population.findSolution():
            printGeneration(generation_counter, population)
            print("### solution found ###")
            break

        generation_counter += 1
        population_gen = population.evolution()
        population = Population(row_num, col_num, garden_matrix, population_gen)
        population.evaluatePopulation()
        printGeneration(generation_counter, population)

        if generation_counter == generation_limit:
            print("### limit of generations ###")

    end_time = time.time()
    duration = end_time - start_time  # Convert to nanoseconds
    print(f"Time taken: {duration} seconds")
    print()


if __name__ == '__main__':
    main()
