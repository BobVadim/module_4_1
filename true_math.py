from math import inf


def divide(first, second):
    if second != 0:
        print(first / second)
    else:
        return inf


divide(69, 3)
print(divide(69, 0))
