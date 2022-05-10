import sys # sys 불러오기
input = sys.stdin.readline # 가독성을 위해 input에 대입

"""
 [택시]
 graph : 플로이드-워셜 결과 행렬 그래프
 table : 경로표. table[i][j] = i->j로 가기 위해 제일 먼저 거쳐야 하는 정점
 1. i->j의 중간 경로를 i로 초기화
 2. i->k->j가 i->j보다 짧다면 i->j의 중간 경로를 i->k의 중간 경로(table[i][k])로 갱신
    k로 갱신하는게 아니라 table[i][k]로 갱신하는 이유는?
    만약 i->k의 경로가 i->t->k라면 최종 경로는 i->t->k->j
    바로 k로 갱신하면 t를 놓칠 수 있기 때문에 table[i][k]로 갱신
    line 24을 table[i][j] = k로 바꾸면 결과가 어떻게 되는지 확인해보세요
"""

def floyd_warshall(n, graph, table): # 플로이드-워셜 함수 정의
    for k in range(1, n+1): # 1부터 n까지 1씩 증가하는 k값에 대해
        for i in range(1, n+1): # 1부터 n까지 1씩 증가하는 i값에 대해
            for j in range(1, n+1): # 1부터 n까지 1씩 증가하는 j값에 대해
                if graph[i][k] + graph[k][j] < graph[i][j]: # graph[i][k]+graph[k][j]값이 graph[i][j]값보다 작다면
                    graph[i][j] = graph[i][k] + graph[k][j] # graph[i][j]에 graph[i][k]+graph[k][j]값 대입
                    table[i][j] = table[i][k] # table[i][j]에 table[i][k]값 대입
    return # 리턴해줌

INF = 10**5 * 2 # INF값 정의
n, m = map(int, input().split()) # n, m값 입력받음 
graph = [[INF]*(n+1) for _ in range(n+1)] # graph 리스트 생성
table = [[0]*(n+1) for _ in range(n+1)] # table 리스트 생성

for _ in range(m): # m번 반복하는동안 
    a, b, s = map(int, input().split()) # a, b, s값 입력받음
    graph[a][b] = graph[b][a] = s # graph[a][b], graph[b][a]에 s 대입

    table[a][b] = b # table[a][b]에 b값 대입
    table[b][a] = a # table[b][a]에 a값 대입

floyd_warshall(n, graph, table) # 함수 사용

for i in range(1, n+1): # 1부터 n까지 1씩 증가하는 i값에 대해
    table[i][i] = '-' # table[i][i]값에 '-' 대입

for line in table[1:]: # table[1]까지의 원소 line에 대해서
    print(*line[1:]) # line[1]부터 마지막 원소까지 출력(원소만)
