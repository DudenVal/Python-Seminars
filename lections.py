# def sum_numbers(n, y):
#     print(y)
#     summa = 0
#     for i in range(1, n+1):
#         summa += i
#     return summa

# a = sum_numbers(5, 'qwerty')
# print(a)


# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i
#     return res
# print(sum_str('q','e','l'))
# print(sum_str('q','e','l','q','e','l'))


# from modul1 import *  # импортировать все функции(с помощью *)
# import modul1 as m1   # as способ переименования файла
# from modul1 import max1   # вывод функции напрямую
# import modul1  # где modul1 имя файла, откуда импортируем
# # -------------------------------------------------
# print(modul1.max1(5, 9))
# # -------------------------------------------------
# print(max1(13, 9))
# # -------------------------------------------------
# # -------------------------------------------------
# print(m1.max1(15, 9))
# # -----------------------РЕКУРСИЯ--------------------------


# def fib(n):
#     if n in [1, 2]:
#         return 1
#     return fib(n-1) + fib(n-2)


# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
#     print(list_1)

# # ---------------------АЛГОРИТМЫ----------------------------
# # ---------------------Принцип быстрой сортировки----------------------------


# def quick_sort(array):
#     if len(array) <= 1:
#         return array
#     else:
#         pivor = array[0]
#     less = [i for i in array[1:] if i <= pivor]
#     greater = [i for i in array[1:] if i > pivor]
#     return quick_sort(less) + [pivor] + quick_sort(greater)


# print(quick_sort([14, 5, 7, 5, 4, 3, 5, 1]))

# # ---------------------Принцип сортировки----------------------------


# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j += 1
#             k += 1

#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1

#         while j < len(right):
#             nums[k] = left[j]
#             i += 1
#             k += 1

# list_1 = [1,2,2,4,5,51,2,431,25,1,65,1]
# merge_sort(list_1)
# print(list_1)

# # -------------------подсчет времени---------------

# from time import time
# from random import choices
# nums = choices(range(3000), k=2000) #рандомизатор
# start = time()
# print(time() - start)
# # ----------------------Вспомним функции------------------
# def f(x):
#     return x*x
# a = f # переменная 'a' хранит в себе функцию f
# print(type(a(5)))
# print(type(f(5)))

# # ----------------------Небольшой калькулятор------------------
# def calk1(a, b):
#     return a+b
# def calk2(a, b):
#     return a*b
# def math(op, x, y):
#     print(op(x, y))
# math(calk1, 5, 45)

# /////////////////////Функции лямбда/////////////////////////////

# def calk2(a, b):
#     return a*b
# def math(op, x, y):
#     print(op(x, y))

# calk3 = lambda a, b: a + b

# math(calk1, 5, 45)
# # ----------- OR ------------

# def calk2(a, b):
#     return a*b

# def math(op, x, y):
#     print(op(x, y))

# math(lambda a, b: a + b, 5, 45)

# ---------------------Самост решение------------

# list_1 = [1,2,3,5,8,15,23,38]
# res = list()

# for i in list_1:
#     if i % 2 == 0:
#         res.append((i, i**2))

# print(res)

# ----------------------Через лямбду------------------

# def select(f, col):   # Заменяем функцию 'select' на встроенную
#     return [f(x) for x in col]    # функцию 'map'

# def where(f, col):  # Заменяем функцию 'where' на встроенную
#     return [x for x in col if f(x)]  # функцию 'filter'

# list_1 = [1,2,3,5,8,15,23,38]
# res = map(int, list_1)
# print(res)
# res = filter(lambda x: x % 2 == 0, res)
# print(res)
# res = list(map(lambda x: (x, x**2), res))
# print(res)


# /////////////////////Функция 'map'///////////////////////////////

# list_1 = [x for x in range(1, 20)]
# print(list_1)

# list_1 = list(map(lambda x: x+10, list_1))
# #            функция к обьекту, сам объект
# print(list_1)

# ---------------------------ЗАДАЧА ----------------

# data = '15 156 96 3 6 8 52 5'
# print(data)
# data = list(map(int, data.split()))
# print(data)

# /////////////////////////function filter/////////////////////////////

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x%10 == 5, data))
# print(res)


# /////////////////////////function zip////////////////////////////////

# Функция zip() применяется к набору итерируемых объектов и 
# возвращает итератор с кортежами из элементов входных данных

# zip ([1, 2, 3], ['o','l','b'], ['g','R','OY'])
#     [(1, 'o','g'),(2,'l','R'), (3,'b','OY')] 


# ///////////////////////////function enumerate////////////////////////////////////

# Функция enumerate() применяется к итерируемому объекту и 
# возвр-т итер-ор с кортежами из инд-а и эл-тов вход-х данных

# enumerate(['Казань','Смоленск','Рыбки', 'Чикаго'])
# [(0, 'Казань'),(1, 'Смоленск'),(2, 'Рыбки'),(3, 'Чикаго')]

# Другими словами enumirate() позволяет нумеровать набор данных.

# ----------------------РАБОТА С ФАЙЛАМИ--------------------------

# colors = ['red','555','blue']
# data = open('file.txt', 'a') # Тут указываем решим, в котором будем работать
# data.writelines(colors) # Разделителей не будет
# data.close()
#  Чтобы постоянно не закрывать и открывать файл используем:

# with open('file.txt', 'w') as data:   #Идет перезаписть файла('w')
#     data.write('line1\n')
#     data.write('line2\n')

# --------------------------MOD reading------------------

# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

''' 
Это стартовый модуль, задача которого - вызвать метод модуля controller, 
который будет запускать бесконечный цикл, получающий входные "сигналы" 
(из определенного набора) из модуля view (user interface).  

В соответствии с полученной пользователем цифрой controller запускает 
тот или иной метод. 

Все данные телефонного справочника будут представлять собой список словарей. 
Каждый элемент этого списка представляет собой словарь. 

[{<Контакт 1>}, {<Контакт 2>}, {}, ... {Контакт N}]

last_id- глобальная переменная, в которой будет храниться номер последней 
занесенной записи

<Контакт i> = {"ID":<Номер записи>, "Name":<Имя_чел>, "Surname":<Отчество>, ... "Tel":<Телефон>} 

Модуль record. 
В данном модуле описываются функции, определяющие формат записи в базу данных
информации от пользователя (склеивает ключи из словаря и значения из view)

Модуль read (Камянецкий). 
    Например: 
        def view_data (data) : 
        print (data)
        def get_value() : 
        return int(input('value '))

Метод export() 
'''