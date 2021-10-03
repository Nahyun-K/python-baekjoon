# 로프
from sys import stdin
n = int(stdin.readline())
li = []
for i in range(n):
    li.append(int(stdin.readline()))

res = []
li.sort()
for i in range(n):
    res.append(li[i]*(n-i))

print(max(res))
