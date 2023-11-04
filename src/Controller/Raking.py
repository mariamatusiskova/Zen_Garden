import sys

from src.Model import Monk
from src.Model.Way import Way


class Raking:

    def __init__(self, row_val: int, col_val: int, garden_matrix: list):
        self.garden_matrix = garden_matrix
        self.row_val = row_val
        self.col_val = col_val

    def moveForwardDown(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.row_val and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num) and \
            self.garden_matrix[x + 1][y] != 'K'

    def isRockDown(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.row_val and self.garden_matrix[x + 1][y] == 'K' and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num)

    def isZeroDown(self, x: int, y: int) -> bool:
        return x == self.row_val - 1 and self.garden_matrix[x][y] == 0

    def moveDown(self, monk_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_y: bool,
                 initial_pos_down: int) -> (int, int, int, int):
        while monk_pos <= self.row_val:
            if self.moveForwardDown(monk_pos, position, move_num):
                self.garden_matrix[monk_pos][position] = move_num
                monk_pos += 1
            elif self.isRockDown(monk_pos, position, move_num):
                self.garden_matrix[monk_pos][position] = move_num
                current_pos, position = self.rock(monk_pos, position, monk)
                initial_pos = current_pos
                change_y = True
                return current_pos, position, change_y, initial_pos, monk_pos
            elif self.isZeroDown(monk_pos, position):
                self.garden_matrix[monk_pos][position] = move_num
                monk_pos = self.row_val
                return current_pos, position, change_y, initial_pos_down, monk_pos
            else:
                print("reserved")
                for row in self.garden_matrix:
                    for elem in row:
                        if elem == 0:
                            print(".".rjust(2), end="")
                        else:
                            print("{}".format(elem).rjust(2), end="")
                    print()

                exit()

        return current_pos, position, change_y, initial_pos_down, monk_pos

    def moveForwardRight(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.col_val and (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num) and \
            self.garden_matrix[y][x + 1] != 'K'

    def isRockRight(self, x: int, y: int, move_num: int) -> bool:
        return x + 1 < self.col_val and self.garden_matrix[y][x + 1] == 'K' and (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num)

    def isZeroRight(self, x: int, y: int) -> bool:
        return x == self.col_val - 1 and self.garden_matrix[y][x] == 0

    def moveRight(self, monk_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_x: bool,
                  initial_pos_right: int) -> (int, int, int, int, int):
        while monk_pos <= self.col_val:
            if self.moveForwardRight(monk_pos, position, move_num):
                self.garden_matrix[position][monk_pos] = move_num
                monk_pos += 1
            elif self.isRockRight(monk_pos, position, move_num):
                self.garden_matrix[position][monk_pos] = move_num
                position, current_pos = self.rock(position, monk_pos, monk)
                initial_pos_right = current_pos
                change_x = True
                return current_pos, position, change_x, initial_pos_right, monk_pos
            elif self.isZeroRight(monk_pos, position):
                self.garden_matrix[position][monk_pos] = move_num
                monk_pos = self.col_val
                return current_pos, position, change_x, initial_pos_right, monk_pos
            else:
                print("reserved")
                for row in self.garden_matrix:
                    for elem in row:
                        if elem == 0:
                            print(".".rjust(2), end="")
                        else:
                            print("{}".format(elem).rjust(2), end="")
                    print()

                exit()

        return current_pos, position, change_x, initial_pos_right, monk_pos

    def moveForwardUp(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num) and \
            self.garden_matrix[x - 1][y] != 'K'

    def isRockUp(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and self.garden_matrix[x - 1][y] == 'K' and (self.garden_matrix[x][y] == 0 or self.garden_matrix[x][y] == move_num)

    def isZeroUp(self, x: int, y: int) -> bool:
        return x == 0 and self.garden_matrix[x][y] == 0

    def moveUp(self, iter_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_y: bool,
               initial_pos_up: int) -> (int, int, int, int):
        while iter_pos >= 0:
            if self.moveForwardUp(iter_pos, position, move_num):
                self.garden_matrix[iter_pos][position] = move_num
                iter_pos -= 1
            elif self.isRockUp(iter_pos, position, move_num):
                self.garden_matrix[iter_pos][position] = move_num
                current_pos, position = self.rock(iter_pos, position, monk)
                initial_pos_up = current_pos
                change_y = True
                return current_pos, position, change_y, initial_pos_up, iter_pos
            elif self.isZeroUp(iter_pos, position):
                self.garden_matrix[iter_pos][position] = move_num
                iter_pos = 0
                return current_pos, position, change_y, initial_pos_up, iter_pos
            else:
                print("reserved")
                for row in self.garden_matrix:
                    for elem in row:
                        if elem == 0:
                            print(".".rjust(2), end="")
                        else:
                            print("{}".format(elem).rjust(2), end="")
                    print()

                exit()

        return current_pos, position, change_y, initial_pos_up, iter_pos

    def moveForwardLeft(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num) and \
            self.garden_matrix[y][x - 1] != 'K'

    def isRockLeft(self, x: int, y: int, move_num: int) -> bool:
        return x - 1 >= 0 and self.garden_matrix[y][x - 1] == 'K' and (self.garden_matrix[y][x] == 0 or self.garden_matrix[y][x] == move_num)

    def isZeroLeft(self, x: int, y: int) -> bool:
        return x == 0 and self.garden_matrix[y][x] == 0

    def moveLeft(self, iter_pos: int, position: int, monk: Monk, move_num: int, current_pos: int, change_x: bool,
                 initial_pos_left: int) -> (int, int, int, int, int):
        while iter_pos >= 0:
            if self.moveForwardLeft(iter_pos, position, move_num):
                self.garden_matrix[position][iter_pos] = move_num
                iter_pos -= 1
            elif self.isRockLeft(iter_pos, position, move_num):
                self.garden_matrix[position][iter_pos] = move_num
                position, current_pos = self.rock(position, iter_pos, monk)
                initial_pos_left = current_pos
                change_x = True
                return current_pos, position, change_x, initial_pos_left, iter_pos
            elif self.isZeroLeft(iter_pos, position):
                self.garden_matrix[position][iter_pos] = move_num
                iter_pos = 0
                return current_pos, position, change_x, initial_pos_left, iter_pos
            else:
                print("reserved")
                for row in self.garden_matrix:
                    for elem in row:
                        if elem == 0:
                            print(".".rjust(2), end="")
                        else:
                            print("{}".format(elem).rjust(2), end="")
                    print()

                exit()

        return current_pos, position, change_x, initial_pos_left, iter_pos

    def swap(self, x: int, y: int) -> (int, int):
        return y, x

    # right/left --> wrong
    def isRocksInTurnY(self, pos_x: int, pos_y: int) -> (str, int, int):
        pos_x, pos_y = self.swap(pos_x, pos_y)
        if pos_x + 1 <= self.col_val and self.garden_matrix[pos_y][pos_x + 1] == 'K' and pos_x - 1 >= 0 and self.garden_matrix[pos_y][pos_x - 1] == 'K':
            return "0", pos_x, pos_y
        if pos_x + 1 <= self.col_val and self.garden_matrix[pos_y][pos_x + 1] == 'K':
            return "01", pos_x, pos_y
        if pos_x - 1 >= 0 and self.garden_matrix[pos_y][pos_x - 1] == 'K':
            return "10", pos_x, pos_y
        if pos_x + 1 <= self.col_val and self.garden_matrix[pos_y][pos_x + 1] != 'K' and pos_x - 1 >= 0 and self.garden_matrix[pos_y][pos_x - 1] != 'K':
            return "1", pos_x, pos_y

        return "0", pos_x, pos_y

    # up/down
    def isRocksInTurnX(self, pos_x: int, pos_y: int) -> (str, int, int):
        #pos_x, pos_y = self.swap(pos_x, pos_y)
        if pos_x + 1 <= self.row_val and self.garden_matrix[pos_x + 1][pos_y] == 'K' and pos_x - 1 >= 0 and \
                self.garden_matrix[pos_x - 1][pos_y] == 'K':
            return "0", pos_x, pos_y
        if pos_x + 1 <= self.row_val and self.garden_matrix[pos_x + 1][pos_y] == 'K':
            return "00", pos_x, pos_y
        if pos_x - 1 >= 0 and self.garden_matrix[pos_x - 1][pos_y] == 'K':
            return "11", pos_x, pos_y
        if pos_x + 1 <= self.row_val and self.garden_matrix[pos_x + 1][pos_y] != 'K' and pos_x - 1 >= 0 and \
                self.garden_matrix[pos_x - 1][pos_y] != 'K':
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
                print("game over :(")
                exit()

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
                print("game over :(")
                exit()

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

        return move_pos, change_x, change_y, position, initial_pos

    def goToNextMonk(self, gen_list_iterator: list, move_num: int, val: int, position: int) -> (Monk, int, int, int):
        monk = next(gen_list_iterator)
        move_num += 1
        initial_pos = val
        current_pos = 0
        position = int(monk.position, 2)

        return monk, initial_pos, current_pos, move_num, position

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

                if self.isIterEnded(monk_pos, self.row_val):
                    try:
                        monk, initial_pos_down, current_pos, move_num, position = \
                            self.goToNextMonk(gen_list_iterator, move_num, 0, position)
                        continue
                    except StopIteration:
                        print("End of the list.")
                        check_list = False
            # up
            elif self.isUp(direction):
                iter_pos, change_x, change_y, position, initial_pos_up = \
                    self.checkCurrPosX(current_pos, initial_pos_up, change_x, change_y, position)
                current_pos, position, change_y, initial_pos_up, iter_pos = \
                    self.moveUp(iter_pos, position, monk, move_num, current_pos, change_y, initial_pos_up)

                if self.isIterEnded(iter_pos, 0):
                    try:
                        monk, initial_pos_up, current_pos, move_num, position = \
                            self.goToNextMonk(gen_list_iterator, move_num, self.row_val - 1, position)
                        continue
                    except StopIteration:
                        print("End of the list.")
                        check_list = False
            # right
            elif self.isRight(direction):
                monk_pos, change_x, change_y, position, initial_pos_right = \
                    self.checkCurrPosY(current_pos, initial_pos_right, change_x, change_y, position)
                current_pos, position, change_x, initial_pos_right, monk_pos = \
                    self.moveRight(monk_pos, position, monk, move_num, current_pos, change_x, initial_pos_right)

                if self.isIterEnded(monk_pos, self.col_val):
                    try:
                        monk, initial_pos_right, current_pos, move_num, position = \
                            self.goToNextMonk(gen_list_iterator, move_num, 0, position)
                        continue
                    except StopIteration:
                        print("End of the list.")
                        check_list = False
            # left
            elif self.isLeft(direction):
                iter_pos, change_x, change_y, position, initial_pos_left = \
                    self.checkCurrPosY(current_pos, initial_pos_left, change_x, change_y, position)
                current_pos, position, change_x, initial_pos_left, iter_pos = \
                    self.moveLeft(iter_pos, position, monk, move_num, current_pos, change_x, initial_pos_left)

                if self.isIterEnded(iter_pos, 0):
                    try:
                        monk, initial_pos_left, current_pos, move_num, position = \
                            self.goToNextMonk(gen_list_iterator, move_num, self.col_val - 1, position)
                        continue
                    except StopIteration:
                        print("End of the list.")
                        check_list = False

    # rock?
    # raked?
    # game over?

    def work(self):
        move_num = 1
        way = Way(self.row_val, self.col_val, self.garden_matrix)
        initial_pos_down = 0
        initial_pos_right = 0
        initial_pos_up = self.row_val - 1
        initial_pos_left = self.col_val - 1
        current_pos = 0
        change_y = False
        change_x = False

        gen_list_iterator = iter(way.gen_list)
        try:
            monk = next(gen_list_iterator)
        except StopIteration:
            print("No monks in the list.")
            return

        self.raking(gen_list_iterator, monk, initial_pos_down, initial_pos_up, initial_pos_right, initial_pos_left,
                    current_pos, change_y, change_x, move_num)

        for row in self.garden_matrix:
            for elem in row:
                if elem == 0:
                    print(".".rjust(2), end="")
                else:
                    print("{}".format(elem).rjust(2), end="")
            print()
