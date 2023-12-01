
def test(*args):
    print(test)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)

test(3, 56, 'привет', 254,)


# рекурсивная функция  для расчёта факториала
def factorial(n):
    if (n == 1):
        return 1
    else:
        return (n * factorial(n-1))
n = int(input("Введите число:"))
print("Факториал числа равен:")
print(factorial(n))


