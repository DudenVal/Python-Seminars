# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов,
# чем Петя и Сережа вместе?

# *Пример:*
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

# Petya = int(input('Введите сколько Пете придется сделать журавликов: '))
# Katya = int(input('Введите сколько Кате придется сделать журавликов: '))
# Seroga = int(input('Введите сколько Сереже придется сделать журавликов: '))
# print()
# 1+1*2

SumAll = int(input('Введите сколько детям придется делать журавликов: '))
Katya = (SumAll // 3) * 2
Petya = (SumAll-Katya)//2
Seroga = Petya
print('Катя сделала =', Katya, ',', 'Петя сделал =',
    Petya,',', 'Сережа сделал =', Seroga, '.')
