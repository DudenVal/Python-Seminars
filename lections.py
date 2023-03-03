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


from modul1 import *  # импортировать все функции(с помощью *)
import modul1 as m1   # as способ переименования файла
from modul1 import max1   # вывод функции напрямую
import modul1  # где modul1 имя файла, откуда импортируем
# -------------------------------------------------
print(modul1.max1(5, 9))
# -------------------------------------------------
print(max1(13, 9))
# -------------------------------------------------
# -------------------------------------------------
print(m1.max1(15, 9))
# -----------------------РЕКУРСИЯ--------------------------


def fib(n):
    if n in [1, 2]:
        return 1
    return fib(n-1) + fib(n-2)


list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
    print(list_1)

# ---------------------АЛГОРИТМЫ----------------------------
# ---------------------Принцип быстрой сортировки----------------------------


def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivor = array[0]
    less = [i for i in array[1:] if i <= pivor]
    greater = [i for i in array[1:] if i > pivor]
    return quick_sort(less) + [pivor] + quick_sort(greater)


print(quick_sort([14, 5, 7, 5, 4, 3, 5, 1]))

# ---------------------Принцип сортировки----------------------------


def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = left[j]
            i += 1
            k += 1

list_1 = [1,2,2,4,5,51,2,431,25,1,65,1]
merge_sort(list_1)
print(list_1)