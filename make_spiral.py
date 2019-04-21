def spiralize(size):
    if size == 0:
        return []
    if size == 1:
        return [[1]]

    result = [[0 for j in range(size)] for i in range(size)]

    direction = 0  # 0 - right, 1 - down, 2 - left, 3 - up
    i, j = 0, 0
    while True:
        result[i][j] = 1
        if direction == 0:
            if j + 1 == len(result) or j + 2 < len(result) and result[i][j + 2] == 1:
                if i + 2 < len(result) and result[i + 2][j] == 1:
                    break
                direction = 1
                i = i + 1
            else:
                j = j + 1
        elif direction == 1:
            if i + 1 == len(result) or i + 2 < len(result) and result[i + 2][j] == 1:
                if result[i - 1][j - 1] == 1:
                    break
                j = j - 1
                direction = 2
            else:
                i = i + 1
        elif direction == 2:
            if j - 1 < 0 or j - 2 >= 0 and result[i][j - 2] == 1:
                if result[i - 2][j] == 1:
                    break
                i = i - 1
                direction = 3
            else:
                j = j - 1
        else:
            result[i][j] = 1
            if i - 1 < 0 or result[i - 2][j] == 1:
                if result[i + 1][j + 1] == 1:
                    break
                j = j + 1
                direction = 0
            else:
                i = i - 1
    return result
