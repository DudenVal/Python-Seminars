n, m =input().split()
first = [int(i) for i in input().split()]
second = [int(j) for j in input().split()]

print(*sorted(set(first).intersection(second)))