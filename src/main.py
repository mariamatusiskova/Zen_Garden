from src.Controller.Raking import Raking
from src.View.Input import Input


def main():
    input = Input()
    row_num, col_num, garden_matrix = input.openAndProccessFile()
    raking = Raking(row_num, col_num, garden_matrix)
    raking.work()




if __name__ == '__main__':
    main()
