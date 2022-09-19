def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def div(a, b):
    return a / b

def mp(a, b):
    return a * b


input("Введите первое число: ")
x = input(int())
c = input("Введите +, -, *, / в зависимости от того, какое действие нужно произвести с числами: ")
input("Введите второе число: ")
y = input(int())
try:
    if c == "*":
        print(mp(x, y))
    elif c == "+":
        print(plus(x, y))
    elif c == "-":
        print(minus(x, y))
    elif c == "/":
        print(div(x, y))
except ZeroDivisionError:
    print('На 0 делить нельзя!')