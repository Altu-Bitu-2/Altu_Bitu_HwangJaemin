import sys # readline 사용을 위해 sys 불러옴
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
일단 방문할 수 있는 도시를 차례차례 방문해볼까요?
그리고 첫 시작 도시로 다시 돌아왔다면 가는 길을 알게 된 거네요! 어느 곳에서 출발해도 똑같겠어요.
[외판원 순회2]
모든 도시를 방문할 수 있는 사이클을 만들고, 그 중 최소비용을 구한다.
사이클이 형성되므로 출발 도시는 중요하지 않다 -> 0으로 고정
"""

MAX = 10**8 # '각 행렬의 성분은 1,000,000 이하의 양의 정수'

# curr_city: 현재 도시의 index, left: 남은 도시의 수, cost: 현재까지의 경비
def backtracking(count, curr_city, cost): # 가장 적은 비용을 들이는 외판원의 순회 여행 경로를 구하는 함수
    global answer   # 전역변수 선언
    
    if cost > answer:   # 현재까지의 경비가 주어진 조건(각 행렬의 성분이 1,000,000 이하의 양의 정수)에서 벗어나면
        return # 함수 종료

    if count == n - 1:   # 모든 도시를 다 방문했다면 0(출발도시)으로 돌아올 수 있는지 확인
        if matrix[curr_city][0] > 0: # 도시 i에서 다른 곳으로 갈 수 있는 경우
            answer = min(answer, cost + matrix[curr_city][0]) # answer값은 answer과 cost + matrix[curr_city][0] 중 최솟값
        return # 종료

    for next_city in range(n): # n번 반복
        if visited[next_city] or matrix[curr_city][next_city] == 0: # next_city를 방문했거나 curr_city에서 next_city로 가는 것이 불가능한 경우에
            continue # 이후 코드 계속 실행
        visited[next_city] = True # next_city에 방문함
        backtracking(count + 1, next_city, cost + matrix[curr_city][next_city]) # count + 1, next_city, cost + matrix[curr_city][next_city]로 backtracking 함수 실행
        visited[next_city] = False # next_city 방문하지 않음

    return # 종료


# 입력
n = int(input()) # n값(도시의 수) 입력받음
matrix = [list(map(int, input().split())) for _ in range(n)] # 비용 행렬 입력받음

visited = [False] * n # 도시 방문했는지 표시할 리스트 
answer = MAX # answer값을 MAX로 설정해 둠

visited[0] = True # 첫 번째 도시 방문
backtracking(0, 0, 0)   # 0에서 출발해 n - 1개 도시를 방문
print(answer) # 답 출력
