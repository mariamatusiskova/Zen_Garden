from src.Model.Way import Way


class Raking:

    def __init__(self, row_val: int, col_val: int, garden_matrix: list):
        self.garden_matrix = garden_matrix
        self.row_val = row_val
        self.col_val = col_val

    # def checkBoundaries(self):
    #     return position.x < self.row_val & & position.x >= 0 & & position.y < self.col_val & & position.y >= 0;

    def work(self):
        move_num = 1
        way = Way(self.row_val, self.col_val, self.garden_matrix)

        for monk in way.gen_list:
            direction = int(monk.direction, 2)
            position = int(monk.position, 2)
            # down
            if direction == 0b00:  # Monk is moving down
                monk_pos = 0
                while monk_pos < self.row_val:
                    self.garden_matrix[monk_pos][position] = move_num
                    monk_pos += 1
                move_num += 1
            # up
            elif direction == 0b11:
                iter_pos = self.row_val - 1
                while iter_pos >= 0:
                    self.garden_matrix[iter_pos][position] = move_num
                    iter_pos -= 1
                move_num += 1
            # right
            elif direction == 0b01:
                monk_pos = 0
                while monk_pos < self.col_val:
                    self.garden_matrix[position][monk_pos] = move_num
                    monk_pos += 1
                move_num += 1
            # left
            elif direction == 0b10:
                iter_pos = self.col_val - 1
                while iter_pos >= 0:
                    self.garden_matrix[position][iter_pos] = move_num
                    iter_pos -= 1
                move_num += 1

        for row in self.garden_matrix:
            for elem in row:
                if elem == 0:
                    print(".".rjust(2), end="")
                else:
                    print("{}".format(elem).rjust(2), end="")
            print()