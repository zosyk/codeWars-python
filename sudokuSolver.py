import copy

"""return the solved puzzle as a 2d array of 9 x 9"""


def sudoku(puzzle, i=0, j=0):
    if i == 9:
        return puzzle
    ixn, jxn = get_next_indexes(puzzle, i, j)

    if puzzle[i][j] == 0:
        next_number = find_number(puzzle, i, j)
        if next_number == -1:
            return False
        new_puzzle = copy.deepcopy(puzzle)
        new_puzzle[i][j] = next_number
        result = sudoku(new_puzzle, ixn, jxn)
        while not result:
            if next_number == 9:
                return False
            next_number = find_number(puzzle, i, j, next_number + 1)
            if next_number == -1:
                return False
            new_puzzle[i][j] = next_number
            result = sudoku(new_puzzle, ixn, jxn)
        return result
    else:
        return sudoku(puzzle, ixn, jxn)

    return puzzle


def get_next_indexes(puzzle, i, j):
    if j == len(puzzle[i]) - 1:
        i += 1
        j = 0
    else:
        j += 1
    return i, j


def find_number(puzzle, i, j, start=1):
    for n in range(start, 10):
        if check_number(puzzle, i, j, n):
            return n
    return -1


def check_number(puzzle, i, j, n):
    if n in puzzle[i] or n in [row[j] for row in puzzle] or n in get_block(puzzle, i, j):
        return False

    return True


def get_block(puzzle, i, j):
    return [row[ix] for ix in range(j // 3 * 3, j // 3 * 3 + 3) for row in puzzle[i // 3 * 3:i // 3 * 3 + 3]]
