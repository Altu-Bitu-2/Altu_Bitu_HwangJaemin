list = [i for i in range(21)]
for i in range(10):
    a, b = map(int, input().split())
    for i in range((b-a+1)//2):
        c = list[b-i]
        list[b-i] = list[a+i]
        list[a+i] = c
for i in list[1:]:
    print(i, end=' ')
