'''
각 너비마다 배치할 수 있는 경우의 수를 저장해 볼까요?
그 전의 타일에서 특정 타일을 이어 붙인다 생각하면 좋을 것 같아요.
이때, 중복으로 경우를 세지 않도록 주의해야겠어요!'''

import sys
input = sys.stdin.readline

n = int(input())
tile = [0] * (n+1)

if n == 1:
    print(1)
elif n == 2:
    print(3)
else:
    tile[1] = 1
    tile[2] = 3
    for i in range(3, n+1):
        tile[i] = tile[i-1]+tile[i-2]*2
    print(tile[n]%10007)
