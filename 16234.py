import sys # sys 불러옴
from collections import deque # 덱 사용
input = sys.stdin.readline # 편리성을 위해 input에 대입

"""
[인구이동]
0. 인구이동이 일어날 수 있는 나라(처음에는 모든 나라)의 좌표를 좌표 큐에 저장
1. bfs 탐색을 통해 연합을 확인하고, 연합에 포함된 나라의 인구이동을 진행한다.
2. 인구 이동이 있었던 나라는 다음 날에도 인구이동이 시작될 수 있으므로 좌표 큐에 다시 넣어준다.
    -> 직전 이동이 있었던 나라에 대해서만 bfs 탐색 진행
    - 인구 이동이 일어나지 않은 두 나라 사이에서는 다음 날에도 인구이동이 일어날 수 없음
3. 인구이동이 전혀 일어나지 않을 때까지 반복
"""

def bfs(n, left, right, i, j, day): # 너비 우선 탐색 함수
    dr = [-1, 1, 0, 0] # 이동할 방향 정의(좌우)
    dc = [0, 0, -1, 1] # 이동할 방향 정의(상하)

    que = deque() # 비어있는 덱을 만듬
    que.append((i, j)) # 덱에 (i, j)쌍 추가
    total = 0   # 연합의 인구 수 합계
    count = 0   # 연합에 포함된 나라의 수
    cord = []   # 연합에 포함된 나라의 좌표
    
    while que: # 덱에 원소가 없을때까지
        r, c = que.popleft() # r과 c는 due의 가장 왼쪽 원소들
        count += 1 # count 증가시킴
        total += board[r][c] # 각 나라의 인구 수 total에 더하기
        cord.append((r, c)) # cord 리스트에 나라의 좌표 집어넣기

        for x in range(4): # 4번 반복
            new_r = r + dr[x] # 새로운 행 r은 기존 행에 dr리스트 x번째 값을 더함
            new_c = c + dc[x] # 새로운 열 c는 기존 열에 dc리스트 x번째 값을 더함
            if not (0 <= new_r < n and 0 <= new_c < n) or visited[new_r][new_c] == day: # 새로운 행 r이 0보다 크고 n보다 작은 조건을 만족하지 못하거나 new_r, new_c 나라의 방문 여부가 day와 같지 않다면
                continue # 코드 계속

            # 이 때 여기서 visited에 표기를 하면 안됨
            # 현재는 조건에 맞지 않지만, 이후에 연합에 있는 다른 나라에 의해 연합에 들어올 수 있음

            if left <= abs(board[new_r][new_c] - board[r][c]) <= right: # 새로 바뀐 국가의 인구수에서 원래 국가의 인구수를 뺀 절댓값이 left보다 크거나 같고 right보다 작거나 같다면
                que.append((new_r, new_c)) # 덱에 새로운 인구수 추가
                visited[new_r][new_c] = day # 새로 만들어진 국경선 나라 방문 결과를 day로 바꿈

    # 적어도 나라 2개 이상이 모여야 연합을 이루었다고 볼 수 있음
    if count > 1: # 연합 수가 1개가 넘는다면
        avg = total // count # 인구 평균은 전체 인구 수를 나라 수로 나눈 값
        # 인구 이동
        for r, c in cord: # 나라 좌표의 행과 열값에 따라
            board[r][c] = avg # r행 c열 나라의 인구수가 평균값
            # 인구의 이동이 있는 나라는 다음 이동이 시작될 가능성이 있음
            countries.append((r, c)) # r행 c열 나라 추가
    
    return count > 1 # count값이 1보다 큰지 참 거짓 값 반환

def simulation(n, left, right): # 인구 이동 지속일 계산 함수
    day = 0 # 지속일
    while True: # 조건 만족하기 전까지는 무한반복
        size = len(countries)   # 이번에 탐색할 수 있는 나라의 수
        flag = False # 연합을 이루었는지 판단하는 flag
        day += 1 # 지속일 + 1
        for _ in range(size): # 탐색 가능한 나라 수 만큼 반복
            i, j = countries.popleft() # i, j는 countries 덱의 가장 왼쪽 값
            if visited[i][j] == day: # i, j좌표의 나라 방문 여부가 day와 같다면
                continue # 프로그램 계속
            visited[i][j] = day # i j 좌표의 나라 방문 여부에 day값 대입
            if bfs(n, left, right, i, j, day):   # bfs 결과 true면 연합을 이루었다는 의미이므로 flag 표시
                flag = True # flag에 True값 대입

        if not flag: # flag값이 True가 아니라면
            return day - 1 # day-1값 리턴해줌

# 입력
n, left, right = map(int, input().split()) # 나라 수, 땅 크기 입력받음
board = [list(map(int, input().split())) for _ in range(n)] # 각 나라의 인구수 입력받음

visited = [[0]*n for _ in range(n)] # 방문 여부를 저장하는 배열
# 나라
countries = deque([(i, j) for i in range(n) for j in range(n)]) # 나라 좌표 저장

# 연산 + 출력
print(simulation(n, left, right)) # 답 출력
