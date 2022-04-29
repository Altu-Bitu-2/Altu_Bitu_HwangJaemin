# 1484 다이어트

# g = (성원이 현재 몸무게)**2 - (성원이가 기억하고 있던 몸무게)**2
# 두 개의 포인터 중 하나는 성원이의 현재 몸무게**2
# 나머지 하나의 포인터는 성원이가 기억하고 있던 몸무게**2


import sys
input = sys.stdin.readline

g = int(input())
a = 1
b = 1
answer = False

while a+b <= g:
    if a**2-b**2 == g:
        print(a)
        a += 1
        answer = True
    elif a**2-b**2 > g:
        b += 1
    elif a**2-b**2 < g:
        a += 1

if not answer:
    print(-1)
