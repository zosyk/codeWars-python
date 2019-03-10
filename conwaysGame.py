def get_generation(cells, generations):
    if not cells:
        return [[]]

    xm, ym, xM, yM = 0, 0, len(cells[0]), len(cells)
    cells = {(x, y) for y, r in enumerate(cells) for x, v in enumerate(r) if v}
    for g in range(generations):
        cells = {(x, y) for x in range(xm - 1, xM + 2) for y in range(ym - 1, yM + 2)
                 if 2 < len(cells & get_neighbors(x, y)) < 4 + ((x, y) in cells)}
    xm = min(x for x, y in cells)
    ym = min(y for x, y in cells)
    xM = max(x for x, y in cells)
    yM = max(y for x, y in cells)

    return [[int((x, y) in cells) for x in range(xm, xM + 1)] for y in range(ym, yM + 1)]


def get_neighbors(x, y):
    return {(x + n, y + m) for n in range(-1, 2) for m in range(-1, 2)}
