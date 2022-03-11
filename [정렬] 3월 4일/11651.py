import sys

N = int(input())

array = []
for i in range(N):
    x, y = map(int, input().split())
    array.append([y, x])

sortedArray = sorted(array)

for y, x in sortedArray:
    print(x, y)
