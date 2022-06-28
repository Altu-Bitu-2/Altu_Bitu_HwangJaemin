import sys # sys 모듈 불러오기
from collections import deque # 덱 생성을 위해 모듈 불러오기
SIZE = 26 # SIZE 크기 정의

"""
 [프로젝트 스케줄링]
 위상 정렬의 끝나는 정점이 여러 개일 경우, 가장 긴 시간을 선택해야 하기 때문에 정답을 항상 max처리 해주어야 함
 !주의! 입력으로 들어오는 그 전에 해야 할 작업은 0개일 수 있음. 즉 주어지지 않을 수 있음.
"""

def topological_sort(day, indegree, graph): #  위상정렬 + DP
    que = deque() # 덱 생성
    dp = day[:] # dp에 day 리스트의 원소 대입
    ans = 0 # 변수 ans 초기화

    for i in range(SIZE): # 0부터 SIZE-1까지 1씩 증가하는 i에 대해
        if not indegree[i]: # indegree[i] 값이 False라면
            que.append(i) # 덱에 i를 원소로 추가

    while que: # 덱에 원소가 존재하는동안
        curr = que.popleft() # curr에 덱의 가장 왼쪽 원소 뽑아서 저장
        ans = max(ans, dp[curr]) # 정답 갱신 - 마지막 정점이 여러개일 경우, 가장 긴 시간을 선택해야 하기 때문

        for next in graph[curr]: # graph[curr]의 원소 next에 대해
            indegree[next] -= 1 # indegree[next]값 1 감소
            if not indegree[next]: # indegree[next]값이 False라면
                que.append(next) # 덱에 next를 원소로 추가
            dp[next] = max(dp[next], dp[curr] + day[next]) # 다음 정점의 시작 시간 계산 -> 사전 작업 중 가장 늦게 끝난 작업으로 갱신

    return ans # 답 리턴

lines = sys.stdin.readlines() # 입력의 끝이 따로 주어지지 않았기 때문에 한번에 입력 받음
day = [0] * SIZE # day 리스트 생성
indegree = [0] * SIZE # indegree 리스트 생성
graph = [list() for _ in range(SIZE)] # graph 생성

for line in lines: # lines의 원소 line에 대해
    line = line.split() # line을 분해해서 line에 대입
    task_num = ord(line[0]) - ord('A')  # 작업 번호
    day[task_num] = int(line[1])    # 해당 작업에 소요되는 일 수
    
    if len(line) == 2: # 사전 작업이 없다면
        continue # 프로그램 계속

    indegree[task_num] = len(line[2]) # indegree[task_num]에 line[2]의 길이 대입

    for i in line[2]: # line[2]의 원소 i에 대해
        graph[ord(i) - ord('A')].append(task_num) # graph 리스트의 ord(i)-ord('A')번째에 task_num 원소 추가

print(topological_sort(day, indegree, graph)) # 결과 출력
