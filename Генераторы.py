
# Напишите функцию-генератор all_variants, которая будет возвращать все подпоследовательности переданной строки.
# В функцию передаётся только сама строка.
# Примечание
# Используйте оператор yield

def all_variants(text):
    for start in range(len(text)):
        for end in range(start + 1, len(text) + 1):
            yield text[start:end]


for substr in all_variants('abc'):
    if len(substr) == 1:
        print(substr)
for substr in all_variants('abc'):
    if len(substr) == 2:
        print(substr)
for substr in all_variants('abc'):
    if len(substr) == 3:
        print(substr)

# Вывод на консоль:
# a
# b
# c
# ab
# bc
# abc