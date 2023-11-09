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
    population = Population(row_num, col_num, garden_matrix)
    population.evaluatePopulation()
    printGeneration(generation_counter, population)

    while generation_limit > generation_counter:

        if population.findSolution():
            printGeneration(generation_counter, population)
            print("### solution found ###")
            break

        population.evolution()
        population.evaluatePopulation()
        printGeneration(generation_counter, population)
        generation_counter += 1

        if generation_counter == generation_limit:
            print("### limit of generations ###")


if __name__ == '__main__':
    main()
