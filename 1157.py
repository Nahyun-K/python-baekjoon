# 단어 공부
from sys import stdin
word = stdin.readline()
word = word.upper()
count = []
array = []
for i in range(len(word)-1):
    array.append(word[i:i+1])
    
lst = set(array)
lst = list(lst)
for j in lst:
    cnt = 0
    for i in array:
        if i == j:
            cnt += 1
    count.append(cnt)

k = 0
res = 0
for i in count:
    if i == max(count):
        res = count.index(i)
        k += 1

if k >= 2:
    print("?")
else:
    print(lst[res])
