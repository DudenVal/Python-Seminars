from time import time
from random import choices

li = []
user_in = (int(input("Input a number: ")))

start = time()
def sum_dev(num):
    cou = 1
    for i in range(2, int(num ** 0.5)):
        if num % i == 0:
            cou += i + num / i
    return cou

for j in range(10, user_in):
    first = sum_dev(j)
    second = sum_dev(first)
    if second == j and first < second:
        print(j, first)

print(time() - start)