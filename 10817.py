# 세 수
from sys import stdin
array = list(map(int, stdin.readline().split()))
array.sort()
print(array[len(array)-2])
