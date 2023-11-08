from src.Controller.Raking import Raking
from src.Model.Population import Population
from src.View.Input import Input

def main():
    # get input from the file
    input = Input()
    row_num, col_num, garden_matrix = input.openAndProccessFile()

    # initialize population
    population = Population(row_num, col_num, garden_matrix)
    population.evaluatePopulation()

    generation_limit = 500
    generation_counter = 1
    while generation_limit > generation_counter:

        if population.findSolution():
            print("Solution found")
            break

        population.evolution()
        generation_counter += 1


if __name__ == '__main__':
    main()
