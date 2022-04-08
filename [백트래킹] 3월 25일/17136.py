import sys # readline 사용을 위해 sys 불러옴
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
우선 색종이를 모두 붙여보아도 좋을 것 같아요.
이때 "최소" 개수를 사용하려면 어떤 크기의 색종이부터 붙여야 할까요?
1. 붙일 수 있는 색종이의 최소 개수를 구하는 것이므로, 큰 색종이부터 붙여가면서 세어보아야 함
2. 색종이의 개수가 각 5장씩으로 제한되어 있기 때문에, 사용한 색종이의 개수를 기록해야 함
"""

SIZE = 10 # 색종이를 10x10 크기의 종이에 붙이려고 하니까
MAX = 26 # 1이 적힌 모든 칸을 붙이는데 필요한 색종이의 최대 개수


def promising(r, c, paper_size): # (r, c)부터 시작해서 paper_size크기의 색종이를 붙일 수 있는지 확인하는 함수
    for i in range(r, r + paper_size): # r부터 r+paper_size-1까지 
        for j in range(c, c + paper_size): # c부터 c+paper_size-1까지
            if board[i][j] == 0: # [i][j] 위치의 칸에 0이 적혀있으면(종이를 붙이면 안 되는 칸)
                return False # False 반환
    return True # 0이 적혀있지 않으면( = 1이 적혀있다면) True값 반환

def fill_board(r, c, paper_size, num): # board의 (r, c)부터 시작해서 paper_size크기를 num으로 채우는 함수
    for i in range(r, r + paper_size): # r부터 r+paper_size-1까지 
        for j in range(c, c + paper_size): # c부터 c+paper_size-1까지
            board[i][j] = num # [i][j]번째 값에 num 넣기
    return # 종료

def backtracking(idx, count): # 1이 적힌 모든 칸을 붙이는 데 필요한 색종이의 최소 개수를 구하는 함수
    global answer   # 전역변수 사용
    
    if count > answer: # count값이 answer보다 크다면
        return # 종료

    if idx == SIZE * SIZE: # idx 값이 10*10이 되면
        answer = min(answer, count) # answer값은 answer과 count를 비교해서 더 최솟값인 쪽
        return # 종료

    x, y = idx // SIZE, idx % SIZE  # x행 y열
    
    if board[x][y] == 0:    # 현재 칸이 0이라면 넘어감
        backtracking(idx + 1, count) # idx + 1 값으로 함수 실행
        return # 종료

    for i in range(5, 0, -1): # 5부터 0까지 1씩 감소시킬 때
        if x + i > SIZE or y + i > SIZE: # 행+i나 열+i가 SIZE값보다 크다면
            continue # 이후 코드 계속 진행
        if promising(x, y, i) and paper_cnt[i] > 0: # promising 함수 결과값과 paper_cnt[i]값이 0보다 크다면
            paper_cnt[i] -= 1 # paper_cnt[i]값 하나 감소
            fill_board(x, y, i, 0) # fill_board 함수 실행
            backtracking(idx + i, count + 1) # idx+i, count+1 값으로 함수 실행
            paper_cnt[i] += 1 # paper_cnt[i]값 하나 증가
            fill_board(x, y, i, 1) # fill_board 함수 실행

    return # 종료

# 입력
board = [list(map(int, input().split())) for _ in range(SIZE)] # board값 입력받음

paper_cnt = [5] * 6 # 남은 색종이의 수 (index 1~5 사용)
answer = MAX    # 최솟값 갱신할 변수

# 연산
backtracking(0, 0) # 함수 실행

if answer == MAX: # 불가한 경우
    print(-1) # -1 출력
else: # 결과값이 나온 경우
    print(answer) # answer 값 출력
