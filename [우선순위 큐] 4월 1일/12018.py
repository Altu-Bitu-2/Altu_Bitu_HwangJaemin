'''
입력받는 숫자들 헷갈리지 않게 조심!
리듬게임 순위 계산하는 문제처럼 과목 수강 가능 인원수와 가장 높은 마일리지를 고려해서
수강신청을 해야 함.
'''


import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
lst= []
cnt = 0

for i in range(n):
    p, l = map(int, input().split())
    miles = list(map(int, input().split()))
    miles.sort()
    if p >= l:
        for j in range(p-l):
            heapq.heappop(miles)
        lst.append(heapq.heappop(miles))

    else:
        lst.append(1)

lst.sort(reverse = True)
for i in range(n):
    m -= lst.pop()
    if m < 0 :
        break
    cnt += 1

print(cnt)
