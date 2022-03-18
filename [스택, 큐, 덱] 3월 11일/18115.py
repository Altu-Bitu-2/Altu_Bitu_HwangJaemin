from collections import deque

N = int(input())
queue = deque(map(int, input().split()))
after = deque(range(1, N+1)) #1부터 N까지 오름차순으로 저장됨
before = deque()

while queue:
    t = queue.pop() #카드섞은방법 저장한 큐의 맨 마지막 원소
    a = after.popleft() #after의 첫번째원소
    if t == 1:
        before.appendleft(a) #after의 첫번째 원소를 before에 집어넣음
    elif t == 2:
        before.insert(1, a)
    elif t == 3:
        before.append(a)
print(*before)
