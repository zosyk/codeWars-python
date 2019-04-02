get_neighbors = lambda p: [(p[0] + x, p[1] + y) for x in [-1, 0, 1] for y in [-1, 0, 1]]

def break_pieces(shape):
    shape = shape.split('\n')

    square = set()
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == ' ':
                square.add((j, i))
    regions = []

    while square:
        region_square = {square.pop()}
        square.update(region_square)
        size = 0

        while len(region_square) != size:
            size = len(region_square)
            new_region_square = set()
            for p in region_square:
                new_region_square.update(get_neighbors(p))
            region_square = new_region_square & square
        square = square - region_square
        region_square_with_borders = set()
        for p in region_square:
            region_square_with_borders.update(get_neighbors(p))
        xm = min(x for x, y in region_square_with_borders)
        ym = min(y for x, y in region_square_with_borders)
        xM = max(x for x, y in region_square_with_borders)
        yM = max(y for x, y in region_square_with_borders)
        region = [[l for l in row[xm:xM + 1]] for row in shape[ym:yM + 1]]

        for i in range(len(region)):
            for j in range(len(region[i])):
                if (j + xm, i + ym) not in region_square_with_borders:
                    region[i][j] = ' '
        for i in range(len(region)):
            for j in range(len(region[i])):
                if region[i][j] == '+':
                    if '-+-' == ''.join(region[i][j - 1:j + 2]):
                        region[i][j] = '-'
                    elif '|+|' == ''.join(row[j] for row in region[i - 1:i + 2] if j < len(row)):
                        region[i][j] = '|'
        if len(region) > 0 and len(region[0]) > 0:
            regions.append('\n'.join([''.join(row).rstrip() for row in region]))
    return regions
