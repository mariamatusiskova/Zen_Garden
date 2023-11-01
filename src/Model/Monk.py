import random


class Monk:
    def __init__(self, row_size: int, col_size: int):
        self.direction = self.rndDirection()
        self.position = self.rndPosition(row_size, col_size)
        self.turn = None

    def rndDirection(self):
        # 00 - down, 01 - right, 10 - left, 11 - up
        movement = random.randint(0, 3)
        movement_bits = bin(movement)[2:].zfill(2)
        print(f'movement: {movement_bits}')
        return movement_bits

    def rndPosition(self, row_size: int, col_size: int):
        # down and up
        if int(self.direction, 2) == 0b00 or int(self.direction, 2) == 0b11:
            pos = random.randint(0, col_size - 1)
            pos_bits = bin(pos)[2:].zfill(2)
            print(f'pos: {pos_bits}')
            return pos_bits
        else:
            pos = random.randint(0, row_size - 1)
            pos_bits = bin(pos)[2:].zfill(2)
            print(f'pos: {pos_bits}')
            return pos_bits

    # def rndTurn(self):
    #     # left - 0, right - 1
    #     side = random.randint(0, 1)
    #     side_bit = bin(side)
    #     return side_bit


