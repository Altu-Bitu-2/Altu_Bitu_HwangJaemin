# 16236번: 아기 상어
'''
<문제 분석>
N*N 크기 공간에 물고기 M마리, 아기 상어 1마리 있음
아기 상어의 크기는 처음엔 2, 1초에 상하좌우로 인접한 한 칸씩 이동
(자기보다 크기가 큰 물고기가 있는 칸은 지나갈 수 없음.
크기가 같은 물고기는 먹을 순 없지만 칸을 지나갈 수는 있음.)

아기 상어의 이동 방법
- 아기 상어가 있는 공간에 더 이상 먹을 물고기가 없다면 도움 요청
- 1마리 먹을 수 있다면 먹으러 감
- 1마리보다 많이 먹을 수 있다면 거리가 가장 가까운 물고기를 먹으러 감
    거리가 가까운 물고기가 많다면 가장 위에 있는 물고기, 그런 물고기가 여러마리면
    가장 왼쪽에 있는 물고기를 먹음
이동에는 1초가 걸리고 물고기를 먹는데 걸리는 시간은 없음


<코드 구조 설계>
아기 상어로부터 가장 가까운 거리에 있는 모든 물고기를 탐색 (BFS),
이동할 수 있는 곳이 없을 때까지 탐색 반복
우선순위 조건에 맞춰 먹으러 갈 물고기 확정
'''

import sys # sys 불러옴
from collections import deque # 덱 사용을 위해 불러옴
input = sys.stdin.readline # 가독성을 위해 input에 대입

INF = 401 # 공간 최댓값 + 1


def next_pos(n, shark_size, shark, board): # 아기 상어가 다음으로 갈 수 있는 칸 구하는 함수
    dr = [-1, 1, 0, 0] # 이동 방향에 대한 리스트 생성
    dc = [0, 0, -1, 1] # 이동 방향에 대한 리스트 생성

    min_dist = INF # 최소 거리를 공간 최댓값 + 1로 설정해 둠
    que = deque()   # 상어가 갈 수 있는 곳을 저장할 덱 생성
    dist = [[0]*n for _ in range(n)]     # 상어로부터의 거리를 저장할 리스트 생성 - 초기값은 0으로
    pos_list = []    # 상어가 먹을 수 있는 물고기들의 위치

    dist[shark[0]][shark[1]] = 1 # [shark[0]][shark[1]]번째에 있는 dist의 원소는 1
    que.append(shark) # 덱에 shark 추가해줌

    while que: # 덱에 원소가 존재하는 동안 반복
        row, col = que.popleft() # row, col에 덱의 가장 왼쪽값 대입

        if dist[row][col] >= min_dist: # 최단거리 이상은 탐색할 필요 없음
            continue # 뒤의 코드 수행

        for i in range(4): # 0부터 3까지 i의 값을 1씩 증가시키면서 
            nr = row + dr[i] # 새 좌표 생성
            nc = col + dc[i] # 새 좌표 생성
            if not (0 <= nr < n and 0 <= nc < n) or dist[nr][nc] or board[nr][nc] > shark_size: # 주어진 조건을 만족한다면
                continue # 이어서 뒤의 코드 수행

            dist[nr][nc] = dist[row][col] + 1 # nr, nc 좌표의 거리값은 row, col 좌표의 거리값 +1
            
            if board[nr][nc] and board[nr][nc] < shark_size: # 먹을 수 있는 물고기 발견
                pos_list.append((nr, nc)) # 상어가 먹을 수 있는 물고기들의 위치를 저장하는 리스트에 좌표 저장
                min_dist = dist[nr][nc] # 최소 거리를 nr, nc 좌표의 거리로 업데이트함
                continue # 이어서 뒤의 코드 수행
            
            que.append((nr, nc)) # 덱에 nr, nc 좌표 추가

    if not pos_list: # 상어가 갈 수 있는 곳이 없음
        return min_dist, (-1, -1) # 최소 거리와 (-1, -1) 리턴해줌

    pos_list.sort() # 상어가 먹을 수 있는 물고기들의 위치가 저장된 리스트 정렬해줌

    return min_dist - 1, pos_list[0] # 최소 거리-1값과 먹을 수 있는 물고기 위치 중 가장 가까운 곳 반환해줌

def simulation(n, shark, board): # 아기 상어가 몇 초 동안 혼자 물고기를 잡아먹을 수 있는지 구하는 함수
    ans = cnt = 0 # ana, cnt 모두 0으로 초기화
    size = 2 # 아기 상어의 처음 크기

    while True: # 계속 반복
        dist, pos = next_pos(n, size, shark, board) # dist, pos에 각각 함수 리턴값 대입
        if dist == INF: # 더 이상 먹을 수 있는 물고기가 공간에 없음
            break # 과정 종료
        
        ans += dist # 먹을 수 있는 물고기가 남아있다면 ans값에 dist 더하기
        cnt += 1 # cnt값 1 증가
        
        # 상어 크기 증가
        if cnt == size: # cnt값이 size값과 같다면
            cnt = 0 # cnt 값을 0으로 초기화하고
            size += 1 # 아기 상어 크기 증가시켜줌

        # 상어 이동
        board[shark[0]][shark[1]] = 0 # 상어가 이동해서 이전에 있던 칸은 빈 칸이 됨
        shark = pos # 아기 상어 위치에 pos 대입

    return ans # 정답값 리턴해줌

# 입력
n = int(input()) # 공간의 크기를 입력받음
board = [list(map(int, input().split())) for _ in range(n)] # 공간의 상태 입력받음

for i in range(n): # n번 반복
    for j in range(n): # n번 반복
        if board[i][j] == 9: # 공간 i, j 좌표의 값이 9라면
            shark_pos = (i, j) # 아기 상어 위치
            break # 종료

print(simulation(n, shark_pos, board)) # 결과값 출력
