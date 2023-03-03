# Напишите функцию, которая принимает
# одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число,
# которое имеет 2 делителя: 1 и n(само число)

def is_simple(num):
    if num in [2,3]:
        return True
    if num % 2 == 0 or num < 2:
        return False
    else:
        for i in range(3, int(num**0.5) + 1, 2):
            if not num % i == 0:
                return False
    return True
print(is_simple(3))