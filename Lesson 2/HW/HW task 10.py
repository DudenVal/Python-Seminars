# Задача 10.
# На столе лежат n монеток. Некоторые из них лежат вверх решкой,
# а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной. Выведите минимальное количество
# монет, которые нужно перевернуть.

a, Result = int(input('Enter count: ')), 0

for i in range(a):
    temp = int(input('Орлы и решки: '))
    if temp > 0 and temp <= 1:
        Result += 1

print('Необходимо перевернуть = ', a - Result)
