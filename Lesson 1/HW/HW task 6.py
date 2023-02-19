# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером,
# где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

Bilet = int(input('Enter you bilet here: '))
i = 0
SumA = 0
SumB = 0
a = Bilet // 1000
b = Bilet % 1000
while(i < a):
    temp = a % 10
    a = a // 10
    SumA += temp
while(i < b):
    temp = b % 10
    b = b // 10
    SumB += temp
if(SumA == SumB):
    print('YEEEEEEEEES')
else:
    print('NOOOOOOOOOOO')