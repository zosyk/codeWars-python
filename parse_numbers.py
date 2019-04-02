def parse_num(s):
    numbers = '0123456789'
    str_n = ''
    for l in s:
        if l in numbers:
            str_n += l
    result = 0
    for i in range(len(str_n)):
        result = result * 10 + numbers.index(str_n[i])

    return result