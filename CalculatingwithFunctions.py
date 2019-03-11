def zero(func=None):  # your code here
    if func is None:
        return 0
    return func(0)


def one(func=None):  # your code here
    if func is None:
        return 1
    return func(1)


def two(func=None):  # your code here
    if func is None:
        return 2
    return func(2)


def three(func=None):  # your code here
    if func is None:
        return 3
    return func(3)


def four(func=None):  # your code here
    if func is None:
        return 4
    return func(4)


def five(func=None):  # your code here
    if func is None:
        return 5
    return func(5)


def six(func=None):  # your code here
    if func is None:
        return 6
    return func(6)


def seven(func=None):  # your code here
    if func is None:
        return 7
    return func(7)


def eight(func=None):  # your code here
    if func is None:
        return 8
    return func(8)


def nine(func=None):  # your code here
    if func is None:
        return 9
    return func(9)


def plus(b):  # your code here
    def plus_helper(a):
        return a + b

    return plus_helper


def minus(b):  # your code here
    def minus_helper(a):
        return a - b

    return minus_helper


def times(b):  # your code here
    def times_helper(a):
        return a * b

    return times_helper


def divided_by(b):  # your code here
    def divided_by_helper(a):
        return a // b

    return divided_by_helper
