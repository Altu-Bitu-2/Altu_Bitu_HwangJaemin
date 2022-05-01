import sys # sys 불러옴
from collections import deque # 덱 사용
input = sys.stdin.readline # 편의상 input에 대입

"""
[적록색약]
그림의 색을 기준으로 구역을 나누는 문제
1. 적록색약이 아닌 사람 기준으로 구역을 나눈다.
2. 그림의 초록을 모두 빨강으로 바꾼 후, 적록색약인 사람 기준으로 구역을 나눈다.
"""

def bfs(i, j, picture, visited): # 너비 우선 탐색 함수
    dr = [-1, 1, 0, 0] # 이동할 방향 정의(좌우)
    dc = [0, 0, -1, 1] # 이동할 방향 정의(상하)

    que = deque() # 덱 정의
    que.append((i, j)) # 덱에 (i, j) 원소 추가
    visited[i][j] = True # visited[i][j]값을 True로 설정

    while que: # 덱에 원소가 존재하는 동안 반복
        r, c = que.popleft() # r, c에 덱의 가장 왼쪽 원소 대입
        for x in range(4): # x에 0~3까지의 값을 차례로 대입하며 반복
            new_r = r + dr[x] # 새로운 r값은 기존 r에 dr[x]값 더함
            new_c = c + dc[x] # 새로운 c값은 기존 c에 dc[x]값 더함
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c]: # 새 좌표가 범위에 맞지 않거나, 이미 방문했으면
                continue # 프로그램 계속
            if picture[new_r][new_c] != picture[r][c]: # picture 리스트의 [new_r][new_c]값이 [r][c]값과 다르다면
                continue # 프로그램 계속
            visited[new_r][new_c] = True # new_r, new_c 좌표 방문으로 표시
            que.append((new_r, new_c)) # 덱에 (new_r, new_c) 원소 추가

    return # 종료

def count_area(n, picture): # 구간 세는 함수
    visited = [[False]*n for _ in range(n)] # False 원소가 n개 있는 visited 리스트 생성
    area = 0 # 구간 수

    for i in range(n): # i에 0~n-1까지의 값을 차례로 대입하며 반복
        for j in range(n): # j에 0~n-1까지의 값을 차례로 대입하며 반복
            if visited[i][j]: # visited[i][j]값이 True라면
                continue # 프로그램 계속
            
            area += 1 # 구간 하나 증가시킴
            bfs(i, j, picture, visited) # bfs 함수 실행
    
    return area # 구간 수 리턴해줌

def green_to_red(n, picture): # 초록색을 빨간색으로 바꿔주는 함수 
    for i in range(n): # i에 0~n-1까지의 값을 차례로 대입하며 반복
        for j in range(n): # j에 0~n-1까지의 값을 차례로 대입하며 반복
            if picture[i][j] == 'G': # picture[i][j]값이 G(초록색)이라면 R로 변경해줌
                picture[i][j] = 'R'
    
    return picture # picture 리턴

# 입력
n = int(input()) # 그리드 가로세로값
picture = [list(input().rstrip()) for _ in range(n)] # RGB값 입력받음
ans = [] # 결과값 담을 리스트

ans.append(count_area(n, picture)) # 적록색약이 아닌 사람이 봤을 때의 구역의 수 ans 리스트에 추가
picture = green_to_red(n, picture) # picture값을 적록색약인 사람이 봤을 때의 구역 수로 변경
ans.append(count_area(n, picture)) # 그 값을 ans 리스트에 추가해줌

print(*ans) # ans 리스트의 원소만 출력
