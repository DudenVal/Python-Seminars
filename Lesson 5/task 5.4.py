

def reorder(number):
    if number == 0:
        return ""
    strochechka = input()
    return reorder(number - 1) + strochechka

nums = int(input('count'))

print(reorder(nums))