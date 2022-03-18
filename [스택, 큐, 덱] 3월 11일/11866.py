#요세푸스 문제
#힌트 '앞에서 제거하고 다시 뒤에 추가해야 하네요!'
#데크
from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
queue = deque()
result = []
for i in range(N):
    queue.append(i+1)
    
print('<', end='')
while queue:
    for i in range(K-1):
        queue.append(queue[0]) #queue[K-1] 전까지는 queue 맨 뒤에 추가하고 삭제하기
        queue.popleft() #pop()의 반대로, 왼쪽(앞쪽)에서 부터 차례대로 제거와 반환하는 메소드이다
    print(queue.popleft(), end = '')
    if queue:
        print(',', end = ' ')
print('>')
