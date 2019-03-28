def break_pieces(shape):
    shape = shape.split('\n')
    max_length = max(len(row) for row in shape)
    shape = [row + ' ' * (max_length - len(row)) for row in shape]
    unhandled_points = []
    for i in range(len(shape)):
        for j in range(len(shape[i])):
            if shape[i][j] == '+':
                unhandled_points.append(Point(j, i))
    start_point = unhandled_points[0]
    init_point_adjacent(start_point, unhandled_points, shape)

    sub_shapes = []
    while start_point is not None:
        sub_shape = get_sub_shape(start_point, [])
        sub_shapes.append(sub_shape)
        next_point = get_next_start_point(sub_shape)
        remove_used_vertices(start_point)
        start_point = next_point

    # for sub_shape in sub_shapes:
    #     print(sub_shape)

    result = []
    for sub in sub_shapes:
        result.append('\n'.join(create_shape(sub)))

    return result


def get_next_start_point(sub_shape):
    for p in sub_shape:
        if len(p.adjacent) > 2:
            return p


def remove_used_vertices(prev_start_point):
    used_vertices = set()
    init_used_vertices(prev_start_point, used_vertices)

    for point in used_vertices:
        for adj_p in point.adjacent:
            adj_p.adjacent.remove(point)


def init_used_vertices(point, used_vertices):
    if len(point.adjacent) > 2 or point in used_vertices:
        return
    used_vertices.add(point)
    for p in point.adjacent:
        init_used_vertices(p, used_vertices)


def get_sub_shape(point, sub_shape):
    sub_shape.append(point)
    if len(sub_shape) > 2 and sub_shape[0] is sub_shape[-1]:
        return sub_shape

    result = None
    for p in point.adjacent:
        if validate_last_three_vertices(sub_shape) and p not in sub_shape or (len(sub_shape) > 2 and sub_shape[0] is p):
            s = get_sub_shape(p, sub_shape[:])
            if s is not None and (result is None or len(s) < len(result)):
                result = s

    return result


def validate_last_three_vertices(sub_shape):
    if len(sub_shape) < 3:
        return True
    last_vertices = sub_shape[-3:]
    if len(set([p.x for p in last_vertices])) == 1 or len(set([p.y for p in last_vertices])) == 1:
        return False

    return True


def init_point_adjacent(point, unhandled_points, shape):
    if len(unhandled_points) == 0:
        return
    unhandled_points.remove(point)

    for p in unhandled_points:
        x, y = p.x, p.y
        if point.y == y:
            adge = shape[y][min(point.x, x) + 1:max(point.x, x)]
            if all(i == '-' for i in adge):
                point.add_adjacent(p)
        elif point.x == x:
            adge = [row[x] for row in shape]
            adge = adge[min(point.y, y) + 1:max(point.y, y)]
            if all(i == '|' for i in adge):
                point.add_adjacent(p)
    for p in point.adjacent:
        init_point_adjacent(p, unhandled_points, shape)
        p.add_adjacent(point)


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.adjacent = []

    def add_adjacent(self, point):
        self.adjacent.append(point)

    def __str__(self):
        return str((self.x, self.y))

    def __repr__(self):
        return self.__str__()


def create_shape(points):
    points = [(p.x, p.y) for p in points]

    # print("start creating shape from points: " + str(points))
    xm = min(x for x, y in points)
    ym = min(y for x, y in points)
    points = [(x - xm, y - ym) for x, y in points]
    xm, ym = 0, 0
    first_index = points.index((xm, min(y for x, y in points if x == 0)))

    if first_index > 0:
        points = points[first_index:] + points[1:first_index] + [points[first_index]]
    # remove points in the middle
    index = 1
    while index < len(points) - 1:
        three_points = points[index - 1: index + 2]
        if len(set(x for x, y in three_points)) == 1 or len(set(y for x, y in three_points)) == 1:
            points.remove(points[index])
        else:
            index += 1

    xM = max(x for x, y in points) + 1
    yM = max(y for x, y in points) + 1
    # normalization
    shape = []
    for i in range(yM - ym):
        shape.append([' '] * (xM - xm))
    for i in range(len(points)):
        x, y = points[i]
        shape[y][x] = '+'
        if i == 0:
            continue

        prev_x, prev_y = points[i - 1]
        if prev_x == x:
            # connect vertically
            min_y = min(y, prev_y)
            max_y = max(y, prev_y)
            for i in range(min_y + 1, max_y):
                shape[i][x] = '|'
        else:  # connect horizontally
            min_x = min(x, prev_x)
            max_x = max(x, prev_x)
            shape[y] = shape[y][:min_x + 1] + ['-'] * (max_x - min_x - 1) + shape[y][max_x:]
    return [''.join(row).rstrip() for row in shape]
