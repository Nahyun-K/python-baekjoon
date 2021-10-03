# 단어의 개수
from sys import stdin
word = stdin.readline()
array = word.split(' ')
cnt = 0
for i in array:
    if i == '':
        cnt += 1
    elif i == '\n':
        cnt += 1

print(len(array) - cnt)
