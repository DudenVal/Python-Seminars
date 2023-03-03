# n = int(input())
# max_number = 1000
# while n != 0:
# n = int(input())
# if max_number > n:
# max_number = n
# print(max_number)
# # ----------------ревью--------------------
# flag = True
# max_number = 0
# while flag:
# n = int(input())
# if max_number < n:
# max_number = n
# if n == 0:
# flag = False
# print(max_number)
# ------------------Задача 2--------------
n = int(input())
max_number = -1
while n != 0:
    if max_number < n:
        max_number = n 
    n = int(input())     
print(max_number)
