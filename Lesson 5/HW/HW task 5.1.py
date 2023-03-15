# Задача 26: 
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
def degree_of_number(numb, exp):
    if exp == 1:
        return numb
    if exp != 1:
        return numb * degree_of_number(numb, exp - 1)
    
numb = int(input('Enter u number: '))
exp = int(input('Enter u degree of number plz: '))
print(degree_of_number(numb, exp))

