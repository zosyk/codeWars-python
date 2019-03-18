import re
from operator import mul, truediv as div, add, sub

OPS = {'*': mul, '/': div, '-': sub, '+': add}


def calc(expression):
    tokens = re.findall(r'[.\d]+|[()+*/-]', expression)
    return parse_add_sub(tokens, 0)[0]


def parse_add_sub(tokens, index):
    value, index = parse_mul_div(tokens, index)
    while index < len(tokens) and tokens[index] != ")":
        token = tokens[index]
        if token in "-+":
            value2, index = parse_mul_div(tokens, index + 1)
            value = OPS[token](value, value2)
    return value, index


def parse_mul_div(tokens, index):
    value, index = parse_parentheses_minus(tokens, index)
    while index < len(tokens) and tokens[index] in "*/":
        token = tokens[index]
        value2, index = parse_parentheses_minus(tokens, index + 1)
        value = OPS[token](value, value2)

    return value, index


def parse_parentheses_minus(tokens, index):
    token = tokens[index]

    if token == "(":
        value, index = parse_add_sub(tokens, index + 1)
    elif token == "-":
        value, index = parse_parentheses_minus(tokens, index + 1)
        value, index = - value, index - 1
    else:
        value = float(token)

    return value, index + 1
