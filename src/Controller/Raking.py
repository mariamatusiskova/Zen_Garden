from src.Model.Way import Way


class Raking:

    def __init__(self, row_val: int, col_val: int, garden_matrix: list):
        self.garden_matrix = garden_matrix
        self.row_val = row_val
        self.col_val = col_val

    def work(self):
        way = Way(self.row_num, self.col_num, self.garden_matrix)

    # in progress
        # for individual_way in way.gen_list:
        #     if