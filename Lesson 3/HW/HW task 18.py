# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

kol_vo = int(input(' Kol-vo: '))

spisok = [randint(2, 5) for i in range(1, kol_vo + 1)]
print(spisok)
x = int(input('Input your number: '))
interval = 2147483647
mini = 2147483647
for i in spisok:
    if x == i:
        print(i)
        break
    if abs(x - i) < interval:
        interval = x - i
        mini = i
        if interval < abs(x - i):
            interval = abs(x - i)
            mini = i
print(f'mini {mini} interv {interval}')