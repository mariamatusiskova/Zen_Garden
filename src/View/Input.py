import numpy as np


class Input:

    def getMatrixSize(self, file):
        try:
            row, col = map(int, file.readline().split('x'))

            # check input
            if row <= 2 or col <= 2:
                raise ValueError("Not positive integers and smaller than 2")

            zero_matrix = [[0 for _ in range(col)] for _ in range(row)]

            return row, col, zero_matrix

        except FileNotFoundError:
            print("Input file not found.")
            exit()
        except ValueError as exception:
            print(f"Invalid input: {exception}")
            exit()
        except Exception as exception:
            print(f"An error occurred: {exception}")
            exit()
    def getRocks(self, row_size: int, col_size: int, matrix_val: list, file):
        try:
            for line in file:
                x, y = map(int, line.strip().split(','))

                # check input
                if x <= 0 or y <= 0:
                    raise ValueError("Not positive integers")

                # Check if the coordinates are within the matrix bounds
                if 0 <= x < row_size and 0 <= y < col_size:
                    matrix_val[x][y] = 'K'
                else:
                    print(f"Invalid coordinates: ({x}, {y})")

            print('\n### Garden in the beginning ###')
            for row in matrix_val:
                for elem in row:
                    if elem == 0:
                        print(".".rjust(2), end="")
                    else:
                        print("{}".format(elem).rjust(2), end="")
                print()

            return matrix_val

        except FileNotFoundError:
            print("Input file not found.")
        except ValueError as exception:
            print(f"Invalid input: {exception}")
        except Exception as exception:
            print(f"An error occurred: {exception}")

    def createMatrix(self, file):
        row, col, matrix = self.getMatrixSize(file)
        matrix = self.getRocks(row, col, matrix, file)
        return row, col, matrix

    def openAndProccessFile(self):
        file = open('Input/input.txt', 'r')

        row, col, garden = self.createMatrix(file)
        return row, col, garden
