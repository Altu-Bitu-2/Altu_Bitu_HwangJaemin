import sys # sys 불러옴
import heapq as hq # heapq 불러옴
input = sys.stdin.readline # 가독성 위해 input에 대입
INF = 10**5 + 1 # 최댓값 정의

"""
 [물대기]
 각 논들 사이의 간선도 고려하고, 우물을 파는 경우도 고려? -> 복잡
 논에 추가로 모든 우물과 연결되는 수원이 있다고 가정!
 ->직접 논에 우물을 파는 경우는 수원과 각 논 사이의 간선 가중치라고 할 수 있음
 
 0 2 2 2 5
 2 0 3 3 4
 2 3 0 4 4
 2 3 4 0 3
 5 4 4 3 0
 
 인덱스 0 ~ n-1은 논, 인덱스 n은 수원
 1개 이상의 논은 반드시 직접 우물을 파야 하므로 수원(n)에서 시작하는 프림 알고리즘
"""

def prim(size, start, graph): # 프림 알고리즘 정의한 함수
    total = 0 # 전체 비용
    pq = [] # 힙 생성
    visited = [False] * size  # 논 방문 여부
    dist = [INF] * size     # 각 논까지의 비용

    dist[start] = 0 # 시작 지점 0으로 초기화
    hq.heappush(pq, (0, start)) # pq에 (0, start) 집어넣음 

    while pq: # pq에 원소가 존재하는 동안
        cost, curr = hq.heappop(pq) # cost, curr에 pq 안의 값 대입함

        if visited[curr]: # curr 지점에 방문했다면
            continue # 프로그램 계속

        visited[curr] = True # curr 지점 방문했다고 표시
        total += cost # 전체 비용에 cost 더해줌

        for i in range(size): # 0부터 size-1까지 1씩 증가하는 i에 대해서
            if not visited[i] and graph[curr][i] < dist[i]: # i 지점을 방문하지 앟았고 graph[curr][i]값이 dist[i]값보다 작다면
                dist[i] = graph[curr][i] # dist[i]값에 graph[curr][i]값 대입
                hq.heappush(pq, (graph[curr][i], i)) # 힙에 해당 값 저장

    return total # 전체 비용 리턴


# 입력
n = int(input()) # 논의 수 입력받음
cost = [int(input()) for _ in range(n)] # 우물을 파는데 드는 비용 입력받음

graph = [list(map(int, input().split())) for _ in range(n)] # 논들 사이에서 물을 끌어오는 비용

graph.append(cost + [0]) # 수원지로부터 물을 끌어오는 비용
for i in range(n): # 0부터 n-1까지 1씩 증가하는 i에 대해
    graph[i].append(cost[i]) # graph[i]에 cost[i]값 입력

# 연산 & 출력
print(prim(n+1, n, graph)) # 결과 출력
