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

    return "/".join(sorted(result, key=lambda s: (-len(s), s)))


def createMapFromString(s):
    map = {}
    for char in s:
        if char.islower():
            map[char] = map.get(char, 0) + 1
    return map
