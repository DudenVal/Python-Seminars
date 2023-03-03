# Задача 28: 
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

def sum_numb(first, second):
    if second == 0:
        return first
    return sum_numb(first + 1, second - 1)
    
first = int(input('Enter first number: '))
second = int(input('Enter second number: '))
print(sum_numb(first, second))





