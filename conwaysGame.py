import copy


def get_generation(cells, generations):
    cells = copy.deepcopy(cells)
    for g in range(generations):
        extendBoarders(cells)
        cells_snapshot = copy.deepcopy(cells)
        for i in range(len(cells)):
            for j in range(len(cells[i])):
                live_cells = get_live_cells(cells_snapshot, i, j)
                if cells_snapshot[i][j]:
                    if live_cells < 2 or live_cells > 3:
                        cells[i][j] = 0
                elif live_cells == 3:
                    cells[i][j] = 1
    shrinkBorders(cells)
    return cells


def extendBoarders(cells):
    if 1 in cells[0]:
        cells.insert(0, [0] * len(cells[0]))

    if 1 in cells[len(cells) - 1]:
        cells.append([0] * len(cells[0]))

    hasLiveCellsOnStart = False
    hasLiveCellsAtTheEnd = False
    for row in cells:
        if row[0] == 1:
            hasLiveCellsOnStart = True
            break
    for row in cells:
        if row[-1] == 1:
            hasLiveCellsAtTheEnd = True
            break
    for row in cells:
        if hasLiveCellsOnStart:
            row.insert(0, 0)
        if hasLiveCellsAtTheEnd:
            row.append(0)


def shrinkBorders(cells):
    while len(cells) > 0 and 1 not in cells[0]:
        del cells[0]
    while len(cells) > 0 and 1 not in cells[len(cells) - 1]:
        del cells[len(cells) - 1]

    hasLiveCellsOnStart = False
    while not hasLiveCellsOnStart:
        for row in cells:
            if row[0] == 1:
                hasLiveCellsOnStart = True
                break
        if not hasLiveCellsOnStart:
            for row in cells:
                del row[0]

    hasLiveCellsAtTheEnd = False
    while not hasLiveCellsAtTheEnd:
        for row in cells:
            if row[-1] == 1:
                hasLiveCellsAtTheEnd = True
                break
        if not hasLiveCellsAtTheEnd:
            for row in cells:
                del row[-1]


def get_live_cells(cells, i, j):
    result = 0
    if i - 1 >= 0 and j - 1 >= 0:
        result += cells[i - 1][j - 1]
    if i - 1 >= 0:
        result += cells[i - 1][j]
    if i - 1 >= 0 and j + 1 < len(cells[i]):
        result += cells[i - 1][j + 1]
    if j + 1 < len(cells[i]):
        result += cells[i][j + 1]
    if i + 1 < len(cells) and j + 1 < len(cells[i]):
        result += cells[i + 1][j + 1]
    if i + 1 < len(cells):
        result += cells[i + 1][j]
    if i + 1 < len(cells) and j - 1 >= 0:
        result += cells[i + 1][j - 1]
    if j - 1 >= 0:
        result += cells[i][j - 1]
    return result
