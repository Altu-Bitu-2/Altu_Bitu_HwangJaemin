import sys # sys 모듈 불러옴
from collections import deque # 덱 사용을 위해 모듈 불러옴
input = sys.stdin.readline # input에 대입

"""
[장난감 부품]
- 완제품을 만들기 위해 필요한 기본 부품의 개수를 구하는 문제
- x(만들어지는 부품) <- y(필요한 부품) 의 관계를 역으로 만들면 x -> y가 되면서 루트노드가 완제품이 되고 리프노드가 기본 부품이 됨
- 따라서, BFS/DFS 탐색을 통해 필요한 리프노드의 총 개수를 구함
"""

def bfs(n, graph): # bfs 함수
    que = deque() # 덱 생성
    cnt = [0] * (n + 1) # cnt 리스트 생성
    ans = [0] * (n + 1) # ans 리스트 생성

    que.append(n) # 덱에 원소 n 추가
    cnt[n] = 1  # 큐에 있는 부품 번호에 따른 개수 저장

    while que: # 덱에 원소가 존재한다면
        x = que.popleft() # x에 덱 가장 왼쪽 원소 대입

        if not graph[x]: # 리프노드(기본부품)인 경우
            ans[x] += cnt[x] # ans[x]값에 cnt[x]값 더해줌
            
        for y, k in graph[x]: # 중간부품인 경우
            if not cnt[y]: # 큐에 없으면
                que.append(y) # 삽입해줌
            cnt[y] += k * cnt[x] # cnt[y]에 k*cnt[x]값 더해줌

        cnt[x] = 0  # 처리가 끝나면 0으로 리셋
    return ans # 답 리턴

# 입력
n = int(input()) # 완제품 번호 입력받음
m = int(input()) # 부품들간의 관계가 몇 줄 나올지 입력받음

graph = [list() for _ in range(n+1)] # graph 생성
for _ in range(m): # m번 반복
    x, y, k = map(int, input().split()) # 부품들간의 관계에 관련된 자연수 입력받음
    graph[x].append((y, k)) # 그래프에 원소 추가

# 연산
ans = bfs(n, graph) # 답 대입

# 출력
for i in range(1, n+1): # 1부터 n까지 1씩 증가하는 i에 대해
    if ans[i]: # ans[i]값이 True라면
        print(i, ans[i]) # i, ans[i]값 출력
