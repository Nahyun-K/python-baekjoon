# 신입사원
from sys import stdin
from operator import itemgetter
t = int(stdin.readline())   # 테스트 케이스 개수 1~20

for i in range(t):
    cnt = 1
    n = int(stdin.readline())   # 지원자의 숫자
    people = []
    for j in range(n):
        paper, interview = list(map(int, input().split()))
        people.append([paper, interview])
    people.sort(key=itemgetter(0))
    res = people[0][1]
    for j in range(n):
        if people[j][1] < res:
            cnt += 1
            res = people[j][1]
        else:
            pass
    print(cnt)
