import sys
input = sys.stdin.readline

"""
 [웜홀]
 벨만-포드 문제
 시간이 되돌아가서 출발 지점에 도착하는 경우 = 음의 사이클이 생긴 경우
 특별히 시작점이 주어지지 않았으므로, 벨만-포드를 특정 정점에서 시작하는 경우만 돌릴 시 해당 정점에서 닿을 수 없는 음의 사이클의 존재를 판단할 수 없음
 그러나, 모든 정점에서 벨만-포드 연산을 하게 되면 O(n^2*E)의 시간 복잡도가 걸려서 효율적이지 않음
 => 모든 정점에 도달할 수 있는 임의의 가짜 정점 0을 만들어서 시작점을 0으로 하는 한 번의 벨만-포드 연산으로 그래프 전체에 대한 음의 사이클 존재 여부 판단!
 => 이때, 가짜 정점 0에서 모든 정점으로의 거리가 0인 간선이 있다고 가정하여 dist배열을 0으로 초기화
"""

def bellman_ford(n, edges): # 벨만-포드 함수 정의
    dist = [0] * (n+1)  # 가짜 정점 0에서 모든 정점으로의 거리가 0인 간선이 있다고 가정해 dist 배열을 0으로 초기화

    for i in range(n+1): # n+1만큼 반복
        flag = False # flag값을 False로 설정

        for s, e, t in edges: # 리스트 edges에 저장된 원소 s, e, t에 대해
            if dist[s] + t < dist[e]: # dist[s]+t값이 dist[e]값보다 작다면
                dist[e] = dist[s] + t # dist[e]에 dist[s]+t값 대입
                flag = True # flag를 True로 변경

        if not flag: # flag가 False라면
            return "NO" # 'NO' 출력(출발 위치로 돌아오는 것 불가)

        if i == n: # i값과 n값이 같다면
            return "YES" # 'YES' 출력(출발 위치로 돌아오는 것 가능)

tc = int(input()) # tc값 입력받음
for _ in range(tc): # tc동안 반복

    # 입력
    n, m, w = map(int, input().split()) # n, m, w값 입력받음

    edges = [] # edges 리스트 생성

    for _ in range(m): # m번 반복
        s, e, t = map(int, input().split()) # s, e, t값 입력받음
        edges.append((s, e, t)) # edges 리스트에 (s, e, t)쌍 저장
        edges.append((e, s, t)) # (e, s, t)쌍도 저장

    for _ in range(w): # w만큼 반복
        s, e, t = map(int, input().split()) # s, e, t값 입력받음
        edges.append((s, e, -t)) # edges 리스트에 (s, e, -t)쌍 저장
    
    
    print(bellman_ford(n, edges)) # 결과값 출력
