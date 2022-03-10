n = int(input())

listA = list(map(int, input().split()))
listB = list(map(int, input().split()))

sortedA = sorted(listA, reverse = True)
sortedB = sorted(listB)

s = 0
for i in range(n):
    s += sortedA[i]*sortedB[i]

print(s)
