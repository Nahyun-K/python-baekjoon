n = int(input())
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

print(array)
sum = 0
for i in range(n):
    for j in range(len(array[i])):
        print(array[i][j], end=' ')
        sum += array[i][j]

    print(sum)
