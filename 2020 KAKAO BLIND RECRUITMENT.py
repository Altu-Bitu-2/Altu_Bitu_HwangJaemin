"""
[기둥과 보 설치]
들어오는 입력에 대해 설치 또는 삭제 이후에도 기본 조건에 만족하는지 확인
[기본 조건]
1. 기둥
    a. 바닥 위
    b. 보의 한 쪽 끝
    c. 다른 기둥 위
2. 보
    a. 한쪽 끝이 기둥 위
    b. 양쪽 끝이 보와 연결
- 설치: 설치하려는 좌표가 조건을 만족하는지 확인
- 삭제: 해당 기둥/보를 삭제했을 시 영향을 받는 인접한 기둥/보가 여전히 조건을 만족하고 있는지 확인
"""

board = [] # 2차원 벽면(=배열)

def validate(x, y, a, n): # 현재 상태가 조건에 만족하는지 (x, y) 중심으로 확인하는 함수 
    if a == 0: # 기둥 상태 확인
        if y == 0: # 바닥 위
            return True # 조건 만족
        if board[x][y][1] or (x > 0 and board[x-1][y][1]): # 보의 왼쪽/오른쪽 끝
            return True # 조건 만족
        if y > 0 and board[x][y-1][0]: # 기둥 위
            return True # 조건 만족
        
    else: # 보 상태 확인
        if y > 0 and board[x][y-1][0]: # 왼쪽 끝이 기둥 위(한쪽 끝이 기둥 뒤인 경우)
            return True # 조건 만족
        if x < n and y > 0 and board[x+1][y-1][0]: # 오른쪽 끝이 기둥 위
            return True # 조건 만족
        if 0 < x < n-1 and board[x-1][y][1] and board[x+1][y][1]: # 양쪽 끝이 보와 연결
            return True # 조건 만족
        
    return False # 이외는 조건 불만족

def check_removable(x, y, n): # (x, y)에 있는 구조물을 삭제할 수 있는지 확인
    
    for dx in (-1, 0, 1): # 기둥이 삭제된 경우, 해당 기둥 위에 보가 있었을 수 있으므로 (조건 2-b) 대각선도 확인이 필요
        for dy in (-1, 0, 1): # dy에 차례로 -1, 0, 1 대입
            nx, ny = x+dx, y+dy # nx, ny 선언
            if not (0<= nx <= n and 0 <= ny <= n): # 조건을 만족하지 못한다면
                continue # 이후 코드 이어서 진행
            for j in range(2): # 0부터 1까지 1씩 증가하는 j에 대해
                if board[nx][ny][j] and not validate(nx, ny, j, n): # board[nx][ny][j]가 false고 조건을 만족하지 못한다면
                    return False # False값 반환

    return True # True값 반환

def solution(n, build_frame): # 결과값 반환해주는 함수 정의
    global board # 전역변수 board 정의
    
    board = [[[False] * 2 for _ in range(n+1)] for _ in range(n+1)] # 현재 설치 현황
    answer = [] # 구조물의 상태 저장할 리스트 

    for x, y, a, b in build_frame: # 리스트 build_frame의 원소에 대해서

        if b == 0: # 삭제
            board[x][y][a] = False # 해당 board에 False값 대입
            if not check_removable(x, y, n): # 삭제할 수 없는 경우
                board[x][y][a] = True # 해당 board 값을 True로 해줌

        else: # 설치
            if validate(x, y, a, n): # 설치 가능한 경우
                board[x][y][a] = True # 해당 board에 True값 대입
                
    for i in range(n+1): # 0부터 n까지 1씩 증가하는 i에 대해
        for j in range(n+1): # 0부터 n까지 1씩 증가하는 j에 대해
            for k in range(2): # 0부터 1까지 1씩 증가하는 k
                if board[i][j][k]: # board[i][j][k]값이 True라면(설치 된 상태라면)
                    answer.append([i, j, k]) # 결과값 리스트에 해당 구조물의 상태 추가
    return answer # 결과값 return

if __name__ == "__main__": # 프로그램이 실행되는 경우
    n = 5 # n 정의
    build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]] # build_frame 입력
    print(solution(n, build_frame)) # 결과 출력
