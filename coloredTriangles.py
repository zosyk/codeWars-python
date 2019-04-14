COLORS = {'R', 'G', 'B'}


def triangle(row):
    if len(row) == 1:
        return row

    while len(row) > 1:
        row = ''.join(get_color(row[i - 1], row[i]) for i in range(1, len(row)))

    return row


def get_color(c1, c2):
    if c1 == c2:
        return c1

    return COLORS.difference({c1, c2}).pop()
