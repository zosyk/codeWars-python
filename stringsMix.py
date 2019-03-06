from functools import cmp_to_key


def mix(s1, s2):
    firstMap = createMapFromString(s1)
    secondMap = createMapFromString(s2)
    result = []

    for k, firstValue in firstMap.items():
        secondValue = secondMap.pop(k, 0)
        if firstValue > secondValue and firstValue > 1:
            result.append("1:" + k * firstValue)
        elif secondValue > firstValue:
            result.append("2:" + k * secondValue)
        elif firstValue == secondValue and firstValue > 1:
            result.append("=:" + k * firstValue)
    for k, v in secondMap.items():
        if v > 1:
            result.append("2:" + k * v)

    return "/".join(sorted(result, key=cmp_to_key(cmp_items), reverse=True))


def createMapFromString(s):
    map = {}
    for char in s:
        if char.islower():
            map[char] = map.get(char, 0) + 1
    return map


def cmp_items(a, b):
    if len(a) > len(b):
        return 1
    elif len(a) < len(b):
        return -1
    else:
        if a[0] == "1" and not b[0] == "1":
            return 1
        elif b[0] == "1" and not a[0] == "1":
            return -1
        elif a[0] == "2" and b[0] == "=":
            return 1
        elif a[0] == "=" and b[0] == "2":
            return -1

        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0
