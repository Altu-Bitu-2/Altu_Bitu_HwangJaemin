# 2615번: 오목
'''
<문제 분석>
19*19 크기의 바둑판에 바둑알(흑돌은 1, 백돌은 2로 표시)을 둠
같은 색 바둑알이 연속적으로 다섯 알 놓이면 해당 색이 승리, 단 여섯 알 이상이
연속적으로 놓여 있으면 이긴 것이 아님.
바둑판을 입력받아 흑돌과 백돌 중 어느쪽이 이겼는지, 비겼는지 판단. 한쪽이 이겼다면
다섯 개의 바둑알 중 가장 왼쪽에 있는 바둑알 가로 세로 번호 출력

<코드 구조 설계>
2차원 배열을 사용해 보드 표현
특정 좌표(r, c)를 가장 왼쪽으로 하는 가능한 모든 오목 배치에 대해 오목 여부 확인
가능한 모든 배치 :  오른쪽, 아래, 우하향, 우상향
(6개 이상 연속해 나오는 경우인지 확인하고 해당되면 제해야 함)
'''
import sys # sys 사용을 위해 불러옴
input = sys.stdin.readline # 가독성을 위해 input에 대입

SIZE = 19 # 19*19 바둑판이므로 SIZE에 19 대입


def promising(r, c, stone, board): # 범위와 돌의 종류가 유효한지 확인하는 함수
    return 0 <= r < SIZE and 0 <= c < SIZE and board[r][c] == stone # r, c가 SIZE값보다 작아야 하고 board[r][c]값과 stone값이 같아야 함

def check_dir(r, c, d, board): # 방향 확인 함수
    stone = board[r][c] # 변수 stone에 board[r][c](0, 1, 2 값 중 하나) 대입

    # 가로, 세로, 우하향 대각선, 우상향 대각선
    dr = [0, 1, 1, -1] # 이동 방향에 대한 리스트
    dc = [1, 0, 1, 1] # 이동 방향에 대한 리스트

    if promising(r-dr[d], c-dc[d], stone, board): # r, c 주변 좌표에 대해 범위와 돌의 종류가 유효하다면
        return False # False값 반환
    
    cnt = 0 # (r, c)를 가장 왼쪽으로 하는 이어지는 바둑알의 개수

    while cnt < 6 and promising(r, c, stone, board): # 이어지는 바둑알의 개수가 6개 미만이고 범위/돌의 종류가 유효한 동안에는
        cnt += 1 # 이어지는 바둑알 개수 하나 증가
        r += dr[d] # 방향 배열을 이용해 좌표 r 주변 탐색
        c += dc[d] # 방향 배열을 이용해 좌표 c 주변 탐색
    
    return cnt == 5 # True값 혹은 False값 반환

def is_end(r, c, board): # 승패가 갈려 오목이 끝났는지 판단하는 함수
    # 가로, 세로, 우하향 대각선, 우상향 대각선
    for i in range(4): # 4번 반복
        if check_dir(r, c, i, board): # 방향 확인 함수를 사용하여
            return True # 방향 확인 함수가 True면 True값 반환
    return False # False면 False값 반환

def simulation(board): # 경기 결과를 알려주는 함수
    for i in range(SIZE): # 0부터 SIZE-1까지 1씩 증가하는 i에 대해서
        for j in range(SIZE): # 0부터 SIZE-1까지 1씩 증가하는 j에 대해서
            if not board[i][j]: # 돌이 없는 경우
                continue # 계속함
            if is_end(i, j, board): # 승패가 결정났다면
                return "{}\n{} {}".format(board[i][j], i+1, j+1) # 이긴 돌 색과 가장 왼쪽 돌 좌표 출력

    return 0 # 함수 끝냄

# 입력
board = [list(map(int, input().split())) for _ in range(SIZE)] # 바둑판을 입력받음
# 연산 + 출력
print(simulation(board)) # 결과 출력
