''' 수를 1, 2, 3의 합으로 나타낸 다는 건, 이미 1, 2, 3의 합으로 이루어진 수에서
각각 1과 2와 3을 더해서 나타낸다고 생각해도 좋겠어요!'''

import sys
input = sys.stdin.readline

t = int(input())

def solution(x):
    if x == 1:
        return 1
    elif x == 2:
        return 2
    elif x== 3:
        return 4
    else:
        return solution(x-1) + solution(x-2) + solution(x-3)

for i in range(t):
    n = int(input())
    print(solution(n))
