# 거스름돈
import sys
n = int(sys.stdin.readline())
n = 1000 - n
lst = [500, 100, 50, 10, 5, 1]
i = 0
cnt = 0
while n != 0:
    if n >= lst[i]:
        n = n - lst[i]
        cnt += 1
    else:
        i += 1

print(cnt)
