# Source: https://medium.com/p/e396e98d8bf3 (for understanding genetic algorithm and using the base implementation)
from random import random

from src.Model.Monk import Monk
import random


class Way:
    def __init__(self, row_val: int, col_val: int):
        self.gen_len = random.randint(5, 50)
        self.row_val = row_val
        self.col_val = col_val
        self.gen_list = self.generateGens()

    def generateGens(self):
        monk_list = []
        for idx in range(self.gen_len):
            monk_list.append(Monk(self.row_val, self.col_val))

        return monk_list

