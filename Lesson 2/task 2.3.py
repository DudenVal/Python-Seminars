# Задача 13:
# Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю
# историю наблюдений за погодой. Они обратились к синоптикам,
# а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период,
# в который среднесуточная температура ежедневно
# превышала 0 градусов Цельсия. Напишите программу,
# помогающую синоптикам в работе.

# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.
# Каждое число – среднесуточная температура в соответствующий день.
# Температуры – целые числа и лежат в диапазоне от –50 до 50

# 6 -1 2 3 4 -1 -1 0

number = int(input('Enter number: '))
result = 0
b = 0
for i in range(number):
    temp = int(input('enter temperature: '))
    if temp > 0:
        result += 1
    else:
        if (result > b):
            b = result
        result = 0
print(b)