import sys # sys 불러옴
import heapq as hq # 힙큐 사용을 위해 불러옴
input = sys.stdin.readline # 가독성 위해 input에 대입

"""
[해킹]
- 기본적인 다익스트라 문제
- 우선순위 큐에 삽입을 할 때는 이후 더 빠른 시간이 큐에 들어올 가능성이 있으므로 삽입할 때는 표기하지 않고, 큐에서 제거하는 시점에서 방문 표기 (큐에서 제거하는 시점에는 그때의 시간이 이후로 등장할 수 있는 가장 빠른시간이다.)
 !주의! 그래프 생성 시, a가 b를 의존한다는 건 b 감염 후 a가 감염된다는 뜻이므로 b -> a 방향임
"""

def dijkstra(n, c, graph): # 다익스트라 함수
    visited = [False] * (n+1) # 방문 여부를 체크하기 위해 n+1크기의 리스트 구현

    pq = [(0, c)] # (0, c)를 원소로 가진 리스트 생성
    
    t = 0 # t 생성 후 0 대입
    cnt = 0 # cnt 생성 후 0 대입

    while pq: # 리스트 pq가 비어있지 않을 동안
        curr_t, curr = hq.heappop(pq) # hq에 저장된 쌍을 pop해서 각각 curr_t, curr에 대입
        if visited[curr]: # curr 방문값이 True일 경우
            continue # 다음으로 넘어감
        visited[curr] = True # curr 방문값을 True로 변경
        t = curr_t # t에 curr_t값 대입
        cnt += 1 # cnt값 1 증가
        for next, weight in graph[curr]: # graph[curr]의 원소 next, weight에 대해
            if not visited[next]: # next 방문값이 True라면 
                hq.heappush(pq, (t + weight, next)) # pq 힙에 (t+weight, next)원소 추가
    
    return cnt, t # cnt, t값 리턴


# 입력
t = int(input()) # t값 입력받음

for _ in range(t): # t동안 반복
    # 입력
    n, d, c = map(int, input().split()) # n, d, c값 입력받음
    graph = [[] for _ in range(n+1)] # graph 생성

    # 인접 리스트로 저장
    for _ in range(d): # d만큼 반복
        a, b, s = map(int, input().split()) # a, b, s값 입력받음
        graph[b].append((a, s)) # graph[b]에 (a, s) 추가
    
    # 연산 + 출력
    print(*dijkstra(n, c, graph)) # 결과값 출력
