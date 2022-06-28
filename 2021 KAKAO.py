from itertools import permutations # 순열 사용을 위해 모듈 불러옴
from collections import deque # 덱 사용을 위해 모듈 불러옴

SIZE = 4 # SIZE(격자 가로/세로 크기) 정의
CNT = 6 # CNT(카드 종류) 정의

dr = [-1, 1, 0, 0] # 방향리스트 정의
dc = [0, 0, -1, 1] # 방향리스트 정의

"""
 [카드 짝 맞추기]
 아이디어
 1. 범위가 크지 않음
 2. 존재하는 모든 카드의 종류는 6개, 카드 2장이 한 쌍을 이룬다.
 3. 뒤집을 카드 순서를 정하는 모든 경우의 수는 6!(카드 순서) * 2^6(2개의 카드 중 어떤 카드를 먼저 뒤집을지) -> 브루트포스 가능
 4. 이번에 목표로 하는 카드에 대해 현재 커서에서 목표 카드까지 가는 최단 경로를 구하며 이동 횟수 전부 구하고 최솟값 갱신
 구현
 1. 존재하는 모든 카드의 위치를 저장하며 카드의 개수 세기 (find_cards)
 2. 가능한 모든 카드의 순서(permutations)와 각 카드를 뒤집을 순서(bitmask)를 결정
    ex) seq = {3, 1, 2}, bit = 011 일 때
        3번, 1번, 2번 카드의 순서로 뒤집는다.
        3번 카드는 1번째 카드부터, 1번 카드는 0번째 카드부터, 2번 카드는 1번째 카드부터 뒤집는다.
        bit의 011이 앞에서부터 각각 1, 2, 3번 카드와 대응함
 3. 현재 카드 순서와 각 카드를 뒤집는 순서에 대한 커서 이동 횟수 계산 (match_card)
    현재 커서 위치와 목표 카드 위치에 대해 bfs 함수 실행
    컨트롤 입력을 고려해야 하기 때문에 4방향에 대한 방향 이동에 추가로 컨트롤 입력도 처리한다.(ctrl)
 4. 매 조합에 따라 board가 갱신되므로 board를 복사한 tmp 사용
 공식 풀이 : https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/
"""

def ctrl(row, col, dir, tmp): # 컨트롤로 이동하는 좌표를 리턴하는 함수
    while True: # 무한반복
        row += dr[dir] # dr 리스트의 dir번째 값을 row에 더해줌
        col += dc[dir] # dc 리스트의 dir번째 값을 col에 더해줌
        if not (0 <= row < SIZE) or not(0 <= col < SIZE): # 해당 방향에 카드가 하나도 없다면 그 방향의 가장 마지막 칸으로 이동
            return (row - dr[dir], col - dc[dir]) # 이동한 좌표 리턴
        if tmp[row][col]: # 누른 키 방향에 있는 가장 가까운 카드
            return (row, col) # row, col쌍 리턴


def bfs(r1, c1, r2, c2, tmp): # 현재 커서에서 목표 카드로 이동하는 가장 적은 비용을 리턴하는 함수
    if r1 == r2 and c1 == c2: # 첫 시작 위치에 카드가 있는 경우
        return 1 # 1 리턴

    visited = [[0]*SIZE for _ in range(SIZE)] # 방문 여부 저장 리스트
    que = deque() # 덱 생성
    visited[r1][c1] = 1 # 반드시 엔터를 누르게 될 것. 엔터를 미리 눌렀다 가정하고 1로 표시
    que.append((r1, c1)) # 덱에 r1, c1쌍 추가

    while que: # 덱에 원소가 있는 동안
        row, col = que.popleft() # 덱에서 팝한 원소를 row, col에 저장
        dist = visited[row][col] # dist에 visited[row][col]값 저장
        
        for i in range(4):  # 컨트롤 입력 이동
            nr, nc = ctrl(row, col, i, tmp) # nr, nc에 리턴값 대입
            if not visited[nr][nc]: # nr, nc 좌표를 방문한적이 없다면              
                visited[nr][nc] = dist + 1 # visited[nr][nc]값에 dist+1 대입
                if nr == r2 and nc == c2: # 목표 카드에 도달했다면
                    return dist + 1 # dist+1값 리턴
                que.append((nr, nc)) # 덱에 nr, nc쌍 추가

        for i in range(4): # 방향키 입력 이동
            nr, nc = row + dr[i], col + dc[i] # nr, nc값 대입
            if (0 <= nr < SIZE) and (0 <= nc < SIZE) and not visited[nr][nc]: # nr과 nc 크기가 SIZE보다 작고 nr, nc 위치를 방문하지 않았다면
                if nr == r2 and nc == c2: # 목표 카드에 도달했다면
                    return dist + 1 # dist + 1값 리턴
                visited[nr][nc] = dist + 1 # visited[nr][nc]에 dist + 1값 대입
                que.append((nr, nc)) # 덱에 nr, nc 쌍 추가

    
    return -1 # 목표 카드에 도달하지 못함 (실제로는 일어나지 않는 일)

def match_card(bit, num, r, c, seq, cards, board, answer): # 조합에 대해 카드를 매칭하는 함수
    tmp = [] # 리스트 생성
    for line in board: # board의 원소 line에 대해
        tmp.append(line[:]) # tmp에 line[:] 추가

    ans = 0 # 결과값 초기화
    for i in range(num): # 0부터 num-1까지 1씩 증가하는 i에 대해
        curr = seq[i]   # 이번에 매칭할 캐릭터

        if not cards[curr]: # cards[curr]값이 False라면
            continue # 프로그램 계속

        now = 0 # 해당 캐릭터의 0번째 카드부터 선택한다고 가정
        
         
        if bit & (1 << i): # 만약 해당 위치의 비트가 1을 표시했다면
            now = 1 # 1번째 카드부터 선택

        for _ in range(2): # 두 번 반복
            nr, nc = cards[curr][now]    # 이번에 매칭할 카드 위치
            ans += bfs(r, c, nr, nc, tmp)   # 현재 커서에서 목표 카드까지 이동하는 비용

            if ans >= answer: # 기존 최솟값보다 큰 경우
                return answer # 더 이상의 탐색 불필요

            tmp[nr][nc] = 0 # 카드 삭제
            r, c = nr, nc # 커서 이동
            now = 1 - now   # 다음에 매칭할 카드 인덱스
    
    return ans # ans값 리턴

def find_cards(board): # 존재하는 모든 카드의 위치를 리턴하는 함수
    cards_pos = [list() for _ in range(CNT + 1)]   # 최대 카드 수
    cnt = 0 # cnt값 초기화
    for i in range(SIZE): # 0부터 SIZE-1까지 1씩 증가하는 i에 대해
        for j in range(SIZE): # 0부터 SIZE-1까지 1씩 증가하는 j에 대해
            if not board[i][j]: # board[i][j]값이 False라면
                continue # 프로그램 계속
            cnt = max(cnt, board[i][j]) # cnt 값에 cnt와 board[i][j]중 더 큰 값 대입
            cards_pos[board[i][j]].append((i, j)) # (i, j) 추가
    return cards_pos, cnt # cards_pos와 cnt 값 리턴

def solution(board, r, c): # 답 리턴 함수
    answer = 10**9 # answer값 초기화
    cards, card_cnt = find_cards(board)    # 존재하는 모든 카드의 위치
    
    for seq in permutations(range(1, card_cnt+1), card_cnt): # 가능한 모든 순서에 대해
        for bit in range(1 << card_cnt): # 범위 안에 있는 bit에 대해
            answer = match_card(bit, card_cnt, r, c, seq, cards, board, answer) # answer값에 match_card함수 결과값 대입
    return answer # 답 리턴

if __name__ == "__main__": # 프로그램이 실행되면
    board = [[1, 0, 0, 3], # 격자 
             [2, 0, 0, 0], # 입력
             [0, 0, 0, 2], # 받음
             [3, 0, 1, 0]] # 4*4크기
    print(solution(board, 1, 0)) # 결과 출력
