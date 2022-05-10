import sys # sys 불러오기
from collections import deque # 덱 사용을 위해 불러옴
input = sys.stdin.readline # 가독성 위해 input에 대입

"""
[Puyo Puyo] - bfs, 시뮬레이션 문제
1. bfs 탐색을 통해 4개 이상의 뿌요가 모였는지 확인
2. 4개 이상의 뿌요가 모였다면, 해당되는 영역을 '.'으로 바꾸어 비워줌
3. 전체 필드에 대해 1~2를 다 수행한 후, 뿌요를 떨어뜨림
    - 바닥부터 시작해서 남아있는 뿌요들을 모으고, 남은 부분은 '.'으로 채우는 방식
4. 터뜨릴 수 없을 때까지 반복
여기서, 3번 과정을 편하게 하기 위해 12*6으로 들어오는 입력을 6*12로 바꾸어준다.
같은 열에 있는 데이터를 다루는 것보다 같은 행에 있는 데이터를 다루는 것이 편하기 때문이다.
"""

# 행과 열을 바꾸어 사용하므로 ROW를 6, COL은 12로 설정
ROW = 6 # 좀 더 편하게 수행하기 위해 행의 값을 6으로 변경
COL = 12 # 열의 값을 12로 변경

def bfs(i, j): # 너비 우선 탐색 함수
    dr = [-1, +1, 0, 0] # 상하좌우 이동할 네 방향 정의
    dc = [0, 0, -1, +1] # 마찬가지로 이동할 네 방향 정의
    que = deque() # 덱 만들기
    
    que.append((i, j)) # 덱 que에 i와 j 쌍을 튜플 형태로 저장
    visited = [[False]*COL for _ in range(ROW)] # 방문 표시를 위한 리스트
    visited[i][j] = True # visited[i][j] 방문
    color = board[i][j] # 뿌요 색
    count = 1   # 모여있는 뿌요의 개수
    cords = []  # 포함된 좌표 저장할 리스트

    while que: # 덱 que에 원소가 존재하는 동안 반복
        cords.append(que[0]) # 포함된 좌표 저장할 리스트에 첫 번째 i, j 쌍을 저장
        r, c = que.popleft() # r에 i값, c에 j값이 대입됨
        for x in range(4): # 4번 반복
            nr, nc = r+dr[x], c+dc[x] # r과 c의 새로운 좌표 설정
            if not (0 <= nr < ROW and 0 <= nc < COL): # 새로운 r값이 0보다 크고 ROW보다 작으면서 새로운 c값이 0보다 크고 COL보다 작은게 아니라면
                continue # 아무것도 안하고 넘어감 
            if not visited[nr][nc] and board[nr][nc] == color: # 새로운 좌표에 방문하지 않고 board[nr][nc]값이 color와 같은경우
                visited[nr][nc] = True # nr, nc 좌표 방문으로 변경
                que.append((nr, nc)) # 덱 que에 nr, nc 좌표를 추가함
                count += 1 # count값 1 증가
    
    if count < 4: # count값이 4보다 작은 경우에 
        return False # False(뿌요가 안터지는 경우)

    for r, c in cords: # cords의 r, c값에 대해서
        board[r][c] = '.' # board의 r, c좌표를 '.'으로 함

    return True # count값이 4보다 크거나 같으면 True값 반환


def make_new_board(board): # 뿌요를 터뜨린 이후의 새 필드를 작성하는 함수
    new_board = [] # 새 필드 저장할 리스트
    for i in range(ROW): # ROW값만큼 반복
        temp = [] # temp 리스트 생성
        for j in range(COL): # COL값만큼 반복
            # 남아있는 뿌요를 임시 리스트에 모으기
            if board[i][j] != '.': # i, j좌표값이 '.'가 아니라면
                temp.append(board[i][j]) # temp에 board값 저장
        # 비어 있는 부분을 '.'로 채우기
        while len(temp) < COL: # temp 길이가 COL보다 작은 경우
            temp.append('.') # temp 리스트에 '.' 추가
        new_board.append(temp[:]) # 새 필드를 저장할 리스트에 temp 리스트 추가
    return new_board # 새 필드를 저장한 리스트 리턴해줌

# 입력
board = [[None]*COL for _ in range(ROW)] # None이 COL개 들어있는 리스트가 ROW개 있는 리스트

# 행과 열을 바꾸어 저장
for i in range(COL): # COL값만큼 반복
    line = input().rstrip() # line에 입력값을 저장
    for j in range(ROW): # ROW값만큼 반복
        board[j][12-i-1] = line[j] # board[j][12-i-1]값에 line[j]값 대입
        
ans = 0 # 결과값 0으로 초기화

while True: # 무한반복
    flag = False # flag값 False로 설정
    for i in range(ROW): # ROW값만큼 반복
        for j in range(COL): # COL값만큼 반복
            if board[i][j] == '.': # board[i][j]값이 '.'라면
                continue # 넘어감
            if bfs(i, j): # bfs(i, j)값이 True라면
                flag = True # flag값도 True
    
    if not flag: # flag값이 True라면
        break # 빠져나감
    ans += 1 # 결과값에 1 더해줌
    board = make_new_board(board) # board값을 새로운 board값으로 갱신

print(ans) # 정답 출력
