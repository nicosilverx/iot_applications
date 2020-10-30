def add(arg1, arg2):
    return arg1+arg2

def subtract(arg1, arg2):
    return arg1-arg2

def multiply(arg1, arg2):
    return arg1*arg2

def divide(arg1, arg2):
    return arg1/arg2


if __name__=="__main__":
    a = 3
    b = 4
    ret1 = add(a, b)
    ret2 = subtract(a, b)
    ret3 = multiply(a, b)
    ret4 = divide(a, b)

    print(f"Add: {ret1} Sub: {ret2} Mult: {ret3} Div: {ret4}")