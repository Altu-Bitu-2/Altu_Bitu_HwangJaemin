# 14503: 로봇 청소기

import sys # sys 불러옴
input = sys.stdin.readline # 가독성을 위해 input에 대입

"""
 [로봇 청소기]
 board 정보 -> 0: 빈 칸, 1: 벽, 2: 청소한 공간
 step: 회전 카운트. 4가 되면 한 바퀴 돌아 다시 제자리로 돌아왔음을 의미
 항상 첫 행, 마지막 행, 첫 열, 마지막 열은 벽이라고 문제에서 주어졌으므로 범위 검사를 할 필요가 없음
"""

def cnt_clean_robot(r, c, d, board): # 로봇 청소기가 청소하는 칸의 개수를 계산하는 함수
    # 상, 우, 하, 좌
    dr = [-1, 0, 1, 0] # 이동 방향에 대한 리스트 생성
    dc = [0, 1, 0, -1] # 이동 방향에 대한 리스트 생성

    step = ans = 0 # 회전 카운트와 칸의 개수 선언

    while True: # 계속 반복
        if board[r][c] == 0: # r, c 좌표값의 board가 0(빈 칸)이라면
            board[r][c] = 2 # r, c 좌표를 청소하고 2를 대입해줌
            ans += 1 # 청소한 칸의 개수에 +1 해줌

        if step == 4: # 한 바퀴 돌아 제자리에 돌아왔을 때
            if board[r - dr[d]][c - dc[d]] == 1: # 새로운 좌표가 벽이라면
                return ans # ans값 출력
                
            r -= dr[d] # r값에서 dr[d]값만큼 빼줌
            c -= dc[d] # r값에서 dc[d]값만큼 빼줌
            step = 0
        else: # 이외의 경우
            d = (d + 3) % 4 # d값 갱신
            if board[r + dr[d]][c + dc[d]]: # r+dr[d], c+dc[d] 좌표값이 벽이라면
                step += 1 # 회전 카운트를 하나 더해줌
                continue # 이후 프로그램 계속 실행

            r += dr[d] # r값에 dr[d]값을 더해줌
            c += dc[d] # c값에 dc[d]값을 더해줌
            step = 0 # 회전 카운트 0으로 초기화

# 입력
n, m = map(int, input().split()) # 세로, 가로 크기 입력받음
r, c, d = map(int, input().split()) # 로봇 청소기의 좌표, 바라보는 방향 입력받음

board = [list(map(int, input().split())) for _ in range(n)] # 장소 상태 입력받음

# 연산 + 출력
print(cnt_clean_robot(r, c, d, board)) # 결과 출력
