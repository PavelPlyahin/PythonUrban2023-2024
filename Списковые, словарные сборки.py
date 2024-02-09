def qwadr(x):
    return x * x


def sort(x):
    return x % 2


my_numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

result = map(qwadr, filter(sort, my_numbers))
print(list(result))

