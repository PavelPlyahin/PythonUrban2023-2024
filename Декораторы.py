def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)

        if n == 1:
            raise Exception(f'{n} 1 не может быть простым или составным')

        elif n == 2:
            return f'{n} Простое'
        elif n == 4:
            return f'{n} Составное'
        else:
            for i in range(2, n):
                if n % i == 0:
                    return f'{n} Составное'
                return f'{n} Простое'

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(0, 1, 3))  # 4 Составное
print(sum_three(2, 3, 6))  # 11 Простое
