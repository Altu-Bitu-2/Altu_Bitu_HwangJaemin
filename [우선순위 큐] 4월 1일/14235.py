'''
거점지 방문시 가장 첫 번째 숫자가 보충한 선물 개수이고 그 후로 나오는 수는 선물 가치
선물 가치를 우선순위 큐에 저장하고 0을 만날 때마다 root값 출력
'''


import sys
input = sys.stdin.readline
import heapq

n = int(input())
presents = []
for i in range(n):
    A = list(map(int, input().split()))
    a = A[0]
    if a == 0:
        if presents:
            print(heapq.heappop(presents)[1])
        else:
            print(-1)
    else:
        for j in range(1, a+1):
            heapq.heappush(presents, (-A[j], A[j]))
    
