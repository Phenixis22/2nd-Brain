def create(a: int, b: int) -> list:
    return [a, b]


def add(f1: list, f2: list) -> list:
    return [f1[0]*f2[1] + f2[0]*f1[1], f1[1]*f2[1]]

def sub(f1: list, f2: list) -> list:
    a = f1[0]
    b = f1[1]
    c = f2[0]
    d = f2[1]
    return [f1[0]*f2[1] - f2[0]*f1[1], f1[1]*f2[1]]

def mul(f1: list, f2: list) -> list:
    return [f1[0]*f2[0], f1[1]*f2[1]]

def div(f1: list, f2: list) -> list:
    return mul(f1, [f2[1], f2[0]])

def display(f: list) -> None:
    print(str(f[0]) + '/' + str(f[1]))

def _simplify(f1: list, f2: list) -> list:
    ...