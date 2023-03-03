# Хакер Василий получил доступ к классному
# журналу и хочет заменить все свои минимальные
# оценки на максимальные. Напишите программу,
# которая заменяет оценки Василия,
# но наоборот: все максимальные – на минимальные.

import random

n = int(input('count: '))
array = [random.randint(1, 5) for i in range(n)]
print(array)
num_min = min(array)
num_max = max(array)
num = [num_min if i == num_max else i for i in array]
print(num)