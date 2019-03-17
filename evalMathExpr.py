HIGHER_OPERATIONS = ["*", "/"]
OPERATIONS = ["+", "-"] + HIGHER_OPERATIONS


def calc(expression):
    return calc_helper(expression.replace(" ", ""))


def calc_helper(expression):
    openIdx, closeIdx, openCount, closeCount = 0, 0, 0, 0
    i = 0
    while i < len(expression):
        symbol = expression[i]
        if symbol == "(":
            if openCount == 0:
                openIdx = i
            openCount += 1
        elif symbol == ")":
            closeCount += 1
            if closeCount == openCount:
                openCount, closeCount = 0, 0
                closeIdx = i
                i = openIdx
                subExpr = expression[openIdx: closeIdx + 1]
                expression = expression.replace(subExpr, str(calc(subExpr[1:][:-1])), 1)
        i += 1
    expression = expression.replace("--", "+")
    operations = []
    numbers = []

    start = 0
    for i in range(len(expression)):
        symbol = expression[i]
        if symbol in OPERATIONS and i - start > 0:
            numbers.append(float(expression[start:i]))
            operations.append(symbol)
            start = i + 1
    numbers.append(float(expression[start:]))

    while len(operations) != 0:
        shift = 0
        if len(operations) > 1 and operations[0] not in HIGHER_OPERATIONS and operations[1] in HIGHER_OPERATIONS:
            shift = 1
        operation = operations.pop(shift)
        num1 = numbers.pop(shift)
        num2 = numbers.pop(shift)

        if operation == "-":
            numbers.insert(shift, num1 - num2)
        elif operation == "+":
            numbers.insert(shift, num1 + num2)
        elif operation == "*":
            numbers.insert(shift, num1 * num2)
        elif operation == "/":
            numbers.insert(shift, num1 / num2)

    return numbers.pop()
