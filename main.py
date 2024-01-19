import pickle

kakuro = []


class Cell:

    def __init__(self, black_box, row_sum, column_sum):
        self.black_box = black_box
        self.row_sum = row_sum
        self.column_sum = column_sum
        self.number = -1


def initialize_puzzle():
    puzzle = []
    num_rows = int(input())
    num_columns = int(input())
    for i in range(num_rows):
        row = []
        for j in range(num_columns):
            black_box = int(input())
            row_sum = -1
            column_sum = -1
            if black_box == 1:
                row_sum = int(input())
                column_sum = int(input())
            row.append(Cell(black_box, row_sum, column_sum))
        puzzle.append(row)

    with open("puzzle.bin", "wb") as file:
        pickle.dump(puzzle, file)
        file.close()


def print_puzzle(p):
    num_rows = len(p)
    num_columns = len(p[0])
    for i in range(num_rows):
        for j in range(num_columns):
            cell = p[i][j]
            if cell.black_box == 1:
                print(cell.column_sum, cell.row_sum)
            else:
                print("number", cell.number)


if __name__ == "__main__":
    # initialize_puzzle()
    with open("puzzle.bin", "rb") as f:
        kakuro = pickle.load(f)
        f.close()
    print_puzzle(kakuro)
