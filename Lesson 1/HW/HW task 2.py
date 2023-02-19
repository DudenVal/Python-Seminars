# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

a = int(input('Введите число: '))
b = int(input('Введите число: '))
c = int(input('Введите число: '))

print('Сумма чисел = ',a + b + c)

# -----------------Другое решение------------

Number = int(input('Введите ТРЕХЗНАЧНОЕ число: '))

FirstNumber = Number % 10
SecondNumber = Number // 100
ThirdNumber = Number // 10
ThirdNumber = ThirdNumber % 10
SumNumbers = FirstNumber + SecondNumber + ThirdNumber 
print('Сумма чисел = ',SumNumbers)
# Можно и так, но не читабельно, как по мне
print(SumNumbers((Number//100 + Number//10 % 10 + Number%10)))  

# -----------------Другое решение------------

Number = int(input('Введите число: '))
i = 0
Sum = 0
while(i < Number):
    a = Number % 10
    Number = Number // 10
    Sum += a
print('Сумма чисел = ', Sum)

