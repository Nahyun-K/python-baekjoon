n = int(input())

lst = list(map(int, input().split()))
lst.sort()

sum = 0
for i in range(n):
    for j in range(i+1):
        sum += lst[j]

print(sum)
