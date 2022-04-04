''' 각 수마다 가장 긴 증가하는 부분수열을 저장하며 풀면 될 것 같아요.
어렵다면 깃허브에 올라간 강의자료 피피티를 참고해볼까요!'''

import sys
input = sys.stdin.readline

n = int(input())
listA = list(map(int, input().split()))
dp = [1]*n

for i in range(n):
    for j in range(i):
        if listA[i]>listA[j]:
            dp[i] = max(dp[i], dp[j]+1)
print(max(dp))
