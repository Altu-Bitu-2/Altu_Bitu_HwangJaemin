#그리디 알고리즘
'''
지금 이 순간 최적의 답이 곧 전체 문제의 답인 알고리즘
시간적으로 매우 효율적
모든 순간 답이 되는 방법은 아님

그리디 알고리즘을 적용할 때
- 주로 O(N) 시간복잡도를 가져 입력 범위가 큰 경우가 많음
- 순간의 최적해가 전체 문제의 최적해가 되어야 함
- 그래서 정렬 후 접근하는 문제가 굉장히 많음

순간의 최적해 = 전체 문제의 최적해
- 이를 판단하기 위해선, 수학적 증명이 많이 요구됨(= 판단이 어려움)
- 코딩 테스트의 경우, 비슷한 문제(유명한 그리디 알고리즘 기출 문제 등에서 응용된
문제같은게 나옴)나 직관에 의해 판단할 수 있는 문제가 주로 출제됨
- 결국 연습이 답이고 감을 익히는 수밖에 없음
'''

import sys
input = sys.stdin.readline

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
i = 0
while i < len(price) - 1:
    cost = price[i]
    fuel = 0
    j = i
    while True:
        if j == len(price)-1:
            break
        if cost <= price[j]:
            fuel += length[j]
            j += 1
        else:
            break
    total += (fuel * cost)
    i = j
print(total)
