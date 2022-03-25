#print(a+b) 하지 말고 꼭 직접 구현해주세요!
import sys
a, b = map(int, sys.stdin.readline().split())
listA = list(str(a))
listA.reverse() #한 자리씩 리스트에 저장(str 형태)
listB = list(str(b))
listB.reverse()

if len(listA) > len(listB):
    for i in range(len(listB)):
        listA[i] = int(listA[i])+int(listB[i])
    for t in range(len(listA)-1):
        if listA[t]>=10:
            listA[t+1] += 1
            listA[t] -= 10
    for i in range(len(listA)-1, -1, -1):
        print(listA[i], end='')
    

else:
    for i in range(len(listA)):
        listB[i] = int(listB[i]) + int(listA[i])
    for t in range(len(listB)-1):
        if listB[t]>=10:
            listB[t+1] += 1
            listB[t] -= 10
    for i in range(len(listB)-1, -1, -1):
        print(listB[i], end='')

