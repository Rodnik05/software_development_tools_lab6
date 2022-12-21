def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def div(a, b):
    return a / b


def mul(a, b):
    return a * b 


def calc(a, b, op):
    if op == '+':
        return add(a, b)
    elif op == '-':
        return sub(a, b)
    elif op == '/':
        return div(a, b)
    elif op == '*':
        return mul(a, b)
    else:
        return "Invalid input"


if __name__ == '__main__':
    a, op, b = input().split()
    a = int(a)
    op = str(op)
    b = int(b)
    print(calc(a, b, op))