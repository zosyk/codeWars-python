def get_generation(cells, generations):
    for g in range(generations):
        cells = expand(cells)
        cells = [[next_cell(cells, i, j) for j in range(len(cells[i]))] for i in range(len(cells))]
    trim(cells)
    return cells


def next_cell(cells, i, j):
    live_cells = sum([get(cells, i + x, j + y) for x in range(-1, 2) for y in range(-1, 2)])
    return int(2 < live_cells < 4 + cells[i][j])


def expand(cells):
    row = [0] * (len(cells[0]) + 2)
    return [row] + [[0] + r + [0] for r in cells] + [row]


def trim(cells):
    while not any(cells[0]): del cells[0]
    while not any(cells[-1]): del cells[-1]
    while not any([row[0] for row in cells]): [row.pop(0) for row in cells]
    while not any([row[-1] for row in cells]): [row.pop() for row in cells]


def get(cells, i, j):
    return cells[i][j] if len(cells) > i > -1 < j < len(cells[i]) else 0
