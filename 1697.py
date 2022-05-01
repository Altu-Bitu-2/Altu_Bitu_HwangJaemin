import sys # sys 불러옴
from collections import deque # 덱 사용
input = sys.stdin.readline # input에 대입, 편리성 높여줌

"""
[숨바꼭질]
 x좌표 위에서 x-1, x+1, 2*x의 위치로 계속 이동하며 탐색
 가장 빠른 시간을 찾아야 하므로 주변 노드부터 탐색하는 풀이로 풀어서 k에 도달하면 바로 탐색 종료 (bfs)
"""
SIZE = 10**5 # n과 k의 최댓값이 100,000이므로 SIZE값 10**5로 설정

def bfs(n, k): # 수빈이가 동생을 찾는 가장 빠른 시간을 출력하는 함수
    time = [-1] * (SIZE + 1) # (SIZE+1)개의 -1이 있는 time 리스트 생성
    que = deque() # 덱 생성
    que.append(n) # 덱에 n 추가
    time[n] = 0 # time[n]에 0 대입

    while que: # 덱에 원소가 있다면 반복
        curr = que.popleft() # curr에 덱 가장 왼쪽값 대입
        if curr == k: # curr값이 k값과 같다면
            return time[curr] #time[curr]값 리턴
        
        for next in (curr * 2, curr + 1, curr - 1): # curr*2부터 curr까지 curr-1 간격으로 next 값을 만듬
            if next < 0 or next > SIZE or time[next] > -1: # next가 0보다 작거나 SIZE값보다 크거나, 혹은 time[next]값이 -1보다 크다면
                continue # 프로그램 계속
            time[next] = time[curr] + 1 # time[next] 값에 time[curr] + 1값 대입
            que.append(next) # 덱에 next값 추가

# 입력
n, k = map(int, input().split()) # 수빈이와 수빈이 동생의 위치 입력받음
# 연산 + 출력
print(bfs(n, k)) # 결과 출력
