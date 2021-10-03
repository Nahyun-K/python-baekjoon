# 동전 0      시간초과
from sys import stdin
n, k = map(int, input().split())
lst = [0]*n
for i in range(n):
    a = int(stdin.readline())
    lst.append(a)

cnt = 0
i = 0
while i != n:
    if k >= lst[n-i-1]:
        k = k - lst[n-i-1]
        cnt += 1
    else:
        i += 1
        pass

print(cnt)
