import sys # sys 모듈 불러옴
from collections import deque # 덱 생성을 위한 모듈 불러옴
input = sys.stdin.readline # input에 대입

"""
 [게임 개발]
 - ACM Craft (1005) 와 동일한 문제
 - 최소 시간 = 건물을 동시에 지을 수 있는 건 최대한 동시에 지어야 최소 시간이 걸리므로 그 전 정점 중 가장 오래 걸리는 시간을 선택
"""

def topological_sort(n, time, indegree, graph): # 위상정렬함수
    que = deque() # 덱 생성
    dp = [0] * (n+1) # dp 리스트 생성

    for i in range(1, n+1): # 1부터 n까지 1씩 증가하는 i에 대해
        dp[i] = time[i] # dp[i]에 time[i]값 대입
        if not indegree[i]: # indegree[i]가 False라면
            que.append(i) # 덱에 i를 원소로 추가
    

    while que: # 덱에 원소가 존재하는동안
        curr = que.popleft() # curr에 덱의 가장 왼쪽 원소 뽑아서 저장
        for next in graph[curr]: # graph[curr]의 원소 next에 대해
            indegree[next] -= 1 # indegree[next]값 1 감소시킴
            dp[next] = max(dp[next], dp[curr] + time[next]) # dp[next]에 dp[next]와 dp[curr]+time[next]중 더 큰 값 대입
            if not indegree[next]: # indegree[next]가 False라면
                que.append(next) # 덱에 next를 원소로 추가

    return dp # dp 리턴

# 입력
n = int(input()) # 건물의 종류 수 입력받음
time = [0] * (n+1) # time 리스트 생성
indegree = [0] * (n+1) # indegree 리스트 생성
graph = [list() for _ in range(n+1)] # graph 생성

for i in range(1, n+1): # 1부터 n까지 1씩 증가하는 i에 대해
    line = list(map(int, input().split())) # line에 각 건물을 짓는 시간과 건물을 짓기 위해 먼저 지어져야 하는 건물 번호 주어짐
    time[i] = line[0] # time[i]에 line[0]값 대입
    indegree[i] = len(line) - 2 # indegree[i]값에 len(line) -2 값 대입
    for v in line[1:-1]: # line[1:-1]의 원소 v에 대해
        graph[v].append(i) # graph[v]에 원소 i 추가

print(*topological_sort(n, time, indegree, graph)[1:], sep='\n') # 결과 출력
