from sys import stdin
input = stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

graph.sort()
count = 0
for i in range(n):
    count = 0
    j = i + 1
    if j <= n:
        while i <= n-1:
            if graph[i][1] <= graph[j][0]:
                count += 1
                i = j
            j += 1
            
