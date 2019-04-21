def height(n, m):
    h, t = 0, 1
    for i in range(1, n + 1): 
        t = t * (m - i + 1) // i
        h += t
    return h