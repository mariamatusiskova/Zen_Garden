import sys

from src.Model import Monk
from src.Model.Way import Way


class Raking:

    def __init__(self, row_val: int, col_val: int, garden_matrix: list, way: Way):
        self.garden_matrix = garden_matrix
        self.row_val = row_val
        self.col_val = col_val
        self.game_over = False
        self.solution = False
        self.fitness = 0
        self.way = way

    def checkGameOver(self, pos_x: int, pos_y: int) -> bool:
        return pos_x == -1 and pos_y == -1

    def moveForwardDown(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.row_val and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num) and \
            self.garden_matrix[x + 1][y] != 'K' and self.garden_matrix[x + 1][y] == 0

    def isRockDown(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.row_val and self.garden_matrix[x + 1][y] == 'K' and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num)

    def isZeroDown(self, x: int, y: int) -> bool:
        return x == self.row_val - 1 and self.garden_matrix[x][y] == 0

    def isDifferentMoveNumDown(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.row_val and self.garden_matrix[x + 1][y] != 0 and self.garden_matrix[x + 1][y] != move_num and self.garden_matrix[x + 1][y] != 'K' and self.garden_matrix[x][y] == 0

    def moveDown(self, monk_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_y: bool,
                 initial_pos_down: int) -> (int, int, bool, int, int):
        while monk_pos <= self.row_val:
            if self.moveForwardDown(monk_pos, position, move_num):
                self.garden_matrix[monk_pos][position] = move_num
                monk_pos += 1
            elif self.isRockDown(monk_pos, position, move_num):
                self.garden_matrix[monk_pos][position] = move_num
                current_pos, position = self.rock(monk_pos, position, monk)

                if self.checkGameOver(current_pos, position):
                    return -1, -1, False, -1, -1

                change_y = True
                return current_pos, position, change_y, initial_pos_down, monk_pos
            elif self.isZeroDown(monk_pos, position):
                self.garden_matrix[monk_pos][position] = move_num
                monk_pos = self.row_val
                return current_pos, position, change_y, initial_pos_down, monk_pos
            elif self.isDifferentMoveNumDown(monk_pos, position, move_num):
                self.garden_matrix[monk_pos][position] = move_num
                current_pos, position = self.rock(monk_pos, position, monk)

                if self.checkGameOver(current_pos, position):
                    return -1, -1, False, -1, -1

                change_y = True
                return current_pos, position, change_y, initial_pos_down, monk_pos
            else:
                monk_pos = self.row_val
                return current_pos, position, change_y, initial_pos_down, monk_pos

        return current_pos, position, change_y, initial_pos_down, monk_pos

    def moveForwardRight(self, x: int, y: int, move_num: int) -> bool:
        if 0 <= y < len(self.garden_matrix) and 0 <= x < len(self.garden_matrix[y]):
            return x + 1 < self.col_val and (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num) and \
                x + 1 < len(self.garden_matrix[y]) and self.garden_matrix[y][x + 1] != 'K' and self.garden_matrix[y][
                    x + 1] == 0
        else:
            return False

    def isRockRight(self, x: int, y: int, move_num: int) -> bool:
        if x + 1 < self.col_val and y < len(self.garden_matrix):
            return self.garden_matrix[y][x + 1] == 'K' and (
                        self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num)
        else:
            return False

    def isZeroRight(self, x: int, y: int) -> bool:
        return x == self.col_val - 1 and self.garden_matrix[y][x] == 0

    def isDifferentMoveNumRight(self, x: int, y: int, move_num: int) -> bool:
        if 0 <= x + 1 < self.col_val and 0 <= y < len(self.garden_matrix):
            return (
                    self.garden_matrix[y][x + 1] != 0
                    and self.garden_matrix[y][x + 1] != move_num
                    and self.garden_matrix[y][x + 1] != 'K'
                    and self.garden_matrix[y][x] == 0
            )
        return False

    def moveRight(self, monk_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_x: bool,
                  initial_pos_right: int) -> (int, int, bool, int, int):
        while monk_pos <= self.col_val:
            if self.moveForwardRight(monk_pos, position, move_num):
                self.garden_matrix[position][monk_pos] = move_num
                monk_pos += 1
            elif self.isRockRight(monk_pos, position, move_num):
                self.garden_matrix[position][monk_pos] = move_num
                position, current_pos = self.rock(position, monk_pos, monk)

                if self.checkGameOver(position, current_pos):
                    return -1, -1, False, -1, -1

                change_x = True
                return current_pos, position, change_x, initial_pos_right, monk_pos
            elif self.isZeroRight(monk_pos, position):
                self.garden_matrix[position][monk_pos] = move_num
                monk_pos = self.col_val
                return current_pos, position, change_x, initial_pos_right, monk_pos
            elif self.isDifferentMoveNumRight(monk_pos, position, move_num):
                self.garden_matrix[position][monk_pos] = move_num
                position, current_pos = self.rock(position, monk_pos, monk)

                if self.checkGameOver(position, current_pos):
                    return -1, -1, False, -1, -1

                change_x = True
                return current_pos, position, change_x, initial_pos_right, monk_pos
            else:
                monk_pos = self.col_val
                return current_pos, position, change_x, initial_pos_right, monk_pos

        return current_pos, position, change_x, initial_pos_right, monk_pos

    def moveForwardUp(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num) and \
            self.garden_matrix[x - 1][y] != 'K' and self.garden_matrix[x - 1][y] == 0

    def isRockUp(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and self.garden_matrix[x - 1][y] == 'K' and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num)

    def isZeroUp(self, x: int, y: int) -> bool:
        return x == 0 and self.garden_matrix[x][y] == 0

    def isDifferentMoveNumUp(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and self.garden_matrix[x - 1][y] != 0 and self.garden_matrix[x - 1][y] != move_num and self.garden_matrix[x - 1][y] != 'K' and self.garden_matrix[x][y] == 0

    def moveUp(self, iter_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_y: bool,
               initial_pos_up: int) -> (int, int, bool, int, int):
        while iter_pos >= 0:
            if self.moveForwardUp(iter_pos, position, move_num):
                self.garden_matrix[iter_pos][position] = move_num
                iter_pos -= 1
            elif self.isRockUp(iter_pos, position, move_num):
                self.garden_matrix[iter_pos][position] = move_num
                current_pos, position = self.rock(iter_pos, position, monk)

                if self.checkGameOver(current_pos, position):
                    return -1, -1, False, -1, -1

                change_y = True
                return current_pos, position, change_y, initial_pos_up, iter_pos
            elif self.isZeroUp(iter_pos, position):
                self.garden_matrix[iter_pos][position] = move_num
                iter_pos = 0
                return current_pos, position, change_y, initial_pos_up, iter_pos
            elif self.isDifferentMoveNumUp(iter_pos, position, move_num):
                self.garden_matrix[iter_pos][position] = move_num
                current_pos, position = self.rock(iter_pos, position, monk)

                if self.checkGameOver(current_pos, position):
                    return -1, -1, False, -1, -1

                change_y = True
                return current_pos, position, change_y, initial_pos_up, iter_pos
            else:
                iter_pos = 0
                return current_pos, position, change_y, initial_pos_up, iter_pos

        return current_pos, position, change_y, initial_pos_up, iter_pos

    def moveForwardLeft(self, x: int, y: int, move_num: int) -> bool:
        if 0 <= y < len(self.garden_matrix):
            return x - 1 >= 0 and x - 1 < len(self.garden_matrix[y]) and \
                (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num) and \
                x - 1 >= 0 and self.garden_matrix[y][x - 1] != 'K' and self.garden_matrix[y][x - 1] == 0
        return False

    def isRockLeft(self, x: int, y: int, move_num: int) -> bool:
        if y < 0 or y >= len(self.garden_matrix) or x <= 0 or x >= len(self.garden_matrix[y]):
            return False  # Invalid indices

        return (
                x - 1 >= 0
                and self.garden_matrix[y][x - 1] == 'K'
                and (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num)
        )

    def isZeroLeft(self, x: int, y: int) -> bool:
        return x == 0 and self.garden_matrix[y][x] == 0

    def isDifferentMoveNumLeft(self, x: int, y: int, move_num: int) -> bool:
        if x - 1 >= 0 and y < len(self.garden_matrix) and x - 1 < len(self.garden_matrix[y]):
            return self.garden_matrix[y][x - 1] != 0 and self.garden_matrix[y][x - 1] != move_num and \
                self.garden_matrix[y][x - 1] != 'K' and self.garden_matrix[y][x] == 0
        else:
            return False

    def moveLeft(self, iter_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_x: bool,
                 initial_pos_left: int) -> (int, int, bool, int, int):
        while iter_pos >= 0:
            if self.moveForwardLeft(iter_pos, position, move_num):
                self.garden_matrix[position][iter_pos] = move_num
                iter_pos -= 1
            elif self.isRockLeft(iter_pos, position, move_num):
                self.garden_matrix[position][iter_pos] = move_num
                position, current_pos = self.rock(position, iter_pos, monk)

                if self.checkGameOver(position, current_pos):
                    return -1, -1, False, -1, -1

                change_x = True
                return current_pos, position, change_x, initial_pos_left, iter_pos
            elif self.isZeroLeft(iter_pos, position):
                self.garden_matrix[position][iter_pos] = move_num
                iter_pos = 0
                return current_pos, position, change_x, initial_pos_left, iter_pos
            elif self.isDifferentMoveNumLeft(iter_pos, position, move_num):
                self.garden_matrix[position][iter_pos] = move_num
                position, current_pos = self.rock(position, iter_pos, monk)

                if self.checkGameOver(position, current_pos):
                    return -1, -1, False, -1, -1

                change_x = True
                return current_pos, position, change_x, initial_pos_left, iter_pos
            else:
                iter_pos = 0
                return current_pos, position, change_x, initial_pos_left, iter_pos

        return current_pos, position, change_x, initial_pos_left, iter_pos

    def swap(self, x: int, y: int) -> (int, int):
        return y, x

    # right/left --> wrong
    def isRocksInTurnY(self, pos_x: int, pos_y: int) -> (str, int, int):
        pos_x, pos_y = self.swap(pos_x, pos_y)
        if pos_x + 1 < self.col_val and (self.garden_matrix[pos_y][pos_x + 1] == 'K' or self.garden_matrix[pos_y][pos_x + 1] != 0) and pos_x - 1 >= 0 and self.garden_matrix[pos_y][pos_x - 1] == 'K':
            return "0", pos_x, pos_y
        if pos_x + 1 < self.col_val and (self.garden_matrix[pos_y][pos_x + 1] == 'K' or self.garden_matrix[pos_y][pos_x + 1] != 0):
            return "10", pos_x, pos_y
        if pos_x - 1 >= 0 and (self.garden_matrix[pos_y][pos_x - 1] == 'K' or self.garden_matrix[pos_y][pos_x - 1] != 0):
            return "01", pos_x, pos_y
        if pos_x + 1 < self.col_val and (self.garden_matrix[pos_y][pos_x + 1] != 'K' and self.garden_matrix[pos_y][pos_x + 1] == 0) and pos_x - 1 >= 0 and (self.garden_matrix[pos_y][pos_x - 1] != 'K' and self.garden_matrix[pos_y][pos_x - 1] == 0):
            return "1", pos_x, pos_y

        return "0", pos_x, pos_y

    # up/down
    def isRocksInTurnX(self, pos_x: int, pos_y: int) -> (str, int, int):
        if pos_x + 1 < self.row_val and (self.garden_matrix[pos_x + 1][pos_y] == 'K' or self.garden_matrix[pos_x + 1][pos_y] != 0) and pos_x - 1 >= 0 and \
                self.garden_matrix[pos_x - 1][pos_y] == 'K':
            return "0", pos_x, pos_y
        if pos_x + 1 < self.row_val and (self.garden_matrix[pos_x + 1][pos_y] == 'K' or self.garden_matrix[pos_x + 1][pos_y] != 0):
            return "11", pos_x, pos_y
        if pos_x - 1 >= 0 and (self.garden_matrix[pos_x - 1][pos_y] == 'K' or self.garden_matrix[pos_x - 1][pos_y] != 0):
            return "00", pos_x, pos_y
        if pos_x + 1 < self.row_val and (self.garden_matrix[pos_x + 1][pos_y] != 'K' and self.garden_matrix[pos_x + 1][pos_y] == 0) and pos_x - 1 >= 0 and \
                (self.garden_matrix[pos_x - 1][pos_y] != 'K' and self.garden_matrix[pos_x - 1][pos_y] == 0):
            return "1", pos_x, pos_y

        return "0", pos_x, pos_y

    def rock(self, pos_x: int, pos_y: int, monk: Monk) -> (int, int):
        # change direction, turning
        monk.turn = monk.rndTurn()
        turn = int(monk.turn, 2)
        direction = int(monk.direction, 2)
        if direction == 0b00 or direction == 0b11:
            isRock, pos_x, pos_y = self.isRocksInTurnY(pos_x, pos_y)
            if isRock == "1":
                # Change direction to left or right
                direction = "10" if turn == 0b0 else "01"
            elif isRock == "10":
                direction = "10"
            elif isRock == "01":
                direction = "01"
            else:
                # print("game over :(")
                self.set_fitness()
                return -1, -1

        elif direction == 0b01 or direction == 0b10:
            isRock, pos_x, pos_y = self.isRocksInTurnX(pos_x, pos_y)
            if isRock == "1":
                # Change direction to up or down
                direction = "11" if turn == 0b0 else "00"
            elif isRock == "11":
                direction = "11"
            elif isRock == "00":
                direction = "00"
            else:
                # print("game over :(")
                self.set_fitness()
                return -1, -1

        monk.direction = direction
        return pos_x, pos_y

    def checkCurrPosX(self, current_pos: int, initial_pos: int, change_x: bool, change_y: bool, position: int) -> (
            int, bool, bool, int, int):
        if current_pos == 0 and not change_x:
            move_pos = initial_pos
        elif change_x:
            move_pos = current_pos
            move_pos, position = self.swap(move_pos, position)
            change_x = False
            change_y = False

        return move_pos, change_x, change_y, position, initial_pos

    def checkCurrPosY(self, current_pos: int, initial_pos: int, change_x: bool, change_y: bool, position: int) -> (
            int, bool, bool, int, int):
        if current_pos == 0 and not change_y:
            move_pos = initial_pos
        elif change_y:
            move_pos = current_pos
            change_x = False
            change_y = False

        return move_pos, change_x, change_y, position

    def goToNextMonk(self, gen_list_iterator: list, move_num: int, val: int) -> (Monk, int, int, int, bool, bool):
        monk = next(gen_list_iterator)
        move_num += 1
        initial_pos = val
        current_pos = 0
        position = int(monk.position, 2)
        change_x = False
        change_y = False

        return monk, initial_pos, current_pos, move_num, position, change_x, change_y

    def isDown(self, direction: int) -> bool:
        return direction == 0b00

    def isUp(self, direction: int) -> bool:
        return direction == 0b11

    def isRight(self, direction: int) -> bool:
        return direction == 0b01

    def isLeft(self, direction: int) -> bool:
        return direction == 0b10

    def isIterEnded(self, cmp_val, end_val) -> bool:
        return cmp_val == end_val

    def checkValuesGO(self, x: int, y: int, is_none: bool, z: int, v: int) -> bool:
        return x == -1 and y == -1 and z == -1 and v == -1 and is_none == False

    def raking(self, gen_list_iterator: list, monk: Monk, initial_pos_down: int, initial_pos_up: int,
               initial_pos_right: int, initial_pos_left: int, current_pos: int, change_y: bool, change_x: bool,
               move_num: int):

        position = int(monk.position, 2)
        check_list = True
        while check_list:
            direction = int(monk.direction, 2)
            # down
            if self.isDown(direction):
                monk_pos, change_x, change_y, position, initial_pos_down = \
                    self.checkCurrPosX(current_pos, initial_pos_down, change_x, change_y, position)
                current_pos, position, change_y, initial_pos_down, monk_pos = \
                    self.moveDown(monk_pos, position, monk, move_num, current_pos, change_y, initial_pos_down)

                if self.checkValuesGO(current_pos, position, change_y, initial_pos_down, monk_pos):
                    self.game_over = True
                    return

                if self.isIterEnded(monk_pos, self.row_val):
                    try:
                        monk, initial_pos_down, current_pos, move_num, position, change_x, change_y = \
                            self.goToNextMonk(gen_list_iterator, move_num, 0)
                        # self.printMatrix()
                        continue
                    except StopIteration:
                        # print("End of the list.")
                        check_list = False
            # up
            elif self.isUp(direction):
                iter_pos, change_x, change_y, position, initial_pos_up = \
                    self.checkCurrPosX(current_pos, initial_pos_up, change_x, change_y, position)
                current_pos, position, change_y, initial_pos_up, iter_pos = \
                    self.moveUp(iter_pos, position, monk, move_num, current_pos, change_y, initial_pos_up)

                if self.checkValuesGO(current_pos, position, change_y, initial_pos_up, iter_pos):
                    self.game_over = True
                    return

                if self.isIterEnded(iter_pos, 0):
                    try:
                        monk, initial_pos_up, current_pos, move_num, position, change_x, change_y = \
                            self.goToNextMonk(gen_list_iterator, move_num, self.row_val - 1)
                        # self.printMatrix()
                        continue
                    except StopIteration:
                        # print("End of the list.")
                        check_list = False
            # right
            elif self.isRight(direction):
                monk_pos, change_x, change_y, position = \
                    self.checkCurrPosY(current_pos, initial_pos_right, change_x, change_y, position)
                current_pos, position, change_x, initial_pos_right, monk_pos = \
                    self.moveRight(monk_pos, position, monk, move_num, current_pos, change_x, initial_pos_right)

                if self.checkValuesGO(current_pos, position, change_x, initial_pos_right, monk_pos):
                    self.game_over = True
                    return

                if self.isIterEnded(monk_pos, self.col_val):
                    try:
                        monk, initial_pos_right, current_pos, move_num, position, change_x, change_y = \
                            self.goToNextMonk(gen_list_iterator, move_num, 0)
                        # self.printMatrix()
                        continue
                    except StopIteration:
                        # print("End of the list.")
                        check_list = False
            # left
            elif self.isLeft(direction):
                iter_pos, change_x, change_y, position = \
                    self.checkCurrPosY(current_pos, initial_pos_left, change_x, change_y, position)
                current_pos, position, change_x, initial_pos_left, iter_pos = \
                    self.moveLeft(iter_pos, position, monk, move_num, current_pos, change_x, initial_pos_left)

                if self.checkValuesGO(current_pos, position, change_x, initial_pos_left, iter_pos):
                    self.game_over = True
                    return

                if self.isIterEnded(iter_pos, 0):
                    try:
                        monk, initial_pos_left, current_pos, move_num, position, change_x, change_y = \
                            self.goToNextMonk(gen_list_iterator, move_num, self.col_val - 1)
                        # self.printMatrix()
                        continue
                    except StopIteration:
                       # print("End of the list.")
                        self.set_fitness()
                        check_list = False

    def printMatrix(self):
        print()
        for row in self.garden_matrix:
            for elem in row:
                if elem == 0:
                    print(".".rjust(2), end="  ")
                else:
                    print("{}".format(elem).rjust(2), end="  ")
            print()

    def set_fitness(self):
        count_squares = 0
        for row in self.garden_matrix:
            for elem in row:
                if elem != 0 and elem != 'K':
                    count_squares += 1
        self.fitness = count_squares

    def calculateMaxFitness(self) -> int:
        max = self.row_val * self.col_val

        rock_counter = 0
        for row in self.garden_matrix:
            for elem in row:
                if elem == 'K':
                    rock_counter+= 1

        return max - rock_counter


    def work(self):
        move_num = 1
        initial_pos_down = 0
        initial_pos_right = 0
        initial_pos_up = self.row_val - 1
        initial_pos_left = self.col_val - 1
        current_pos = 0
        change_y = False
        change_x = False

        gen_list_iterator = iter(self.way.gen_list)
        try:
            monk = next(gen_list_iterator)
        except StopIteration:
            print("No monks in the list.")
            return

        self.raking(gen_list_iterator, monk, initial_pos_down, initial_pos_up, initial_pos_right, initial_pos_left,
                    current_pos, change_y, change_x, move_num)

        max_fitness = self.calculateMaxFitness()
        if self.fitness == max_fitness:
            self.solution = True
            self.fitness = max_fitness

        # self.printMatrix()
