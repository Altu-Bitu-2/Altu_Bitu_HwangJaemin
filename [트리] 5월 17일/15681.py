import sys # sys 불러오기
input = sys.stdin.readline # 가독성을 위해 대입
sys.setrecursionlimit(10**8) # 재귀 깊이 설정

"""
 PPT 트리의 정점의 수 구하기 응용
 [트리와 쿼리]
 1. 루트에서부터 dfs 탐색
 2. 각 노드를 루트로 하는 서브트리의 정점 수를 재귀적으로 계산
    - 서브트리에 속한 정점의 개수를 저장하는 dp 배열의 초기화를 -1로 해주고, dfs 탐색 시 현재 정점의 dp 값을 0으로 설정함으로써 자식 노드만 탐색할 수 있도록 함 (부모 노드에 0이 저장되어 있으므로 바로 리턴)
"""

def tree_dp(curr, graph): # 함수 정의
    if subtree_cnt[curr] != -1: # subtree_cnt 리스트의 curr번째 원소가 -1이 아니라면
        return subtree_cnt[curr] # curr번째 원소 리턴

    # 서브트리에 속한 정점의 수를 세고, 저장
    subtree_cnt[curr] = 0   # 현재 노드를 0으로 표기하여 부모 자식간 계속 호출되지 않도록
    cnt = 1 # cnt에 1 대입
    for next in graph[curr]: # graph[curr]의 원소 next에 대해서 
        cnt += tree_dp(next, graph) # cnt에 tree_dp(next, graph)값을 더해줌

    subtree_cnt[curr] = cnt # subtree_cnt[curr]값에 cnt 대입
    return cnt # cnt 리턴해줌 


# 입력
n, r, q = map(int, input().split()) # n, r, p 입력받음
graph = [list() for _ in range(n+1)] # graph 입력받음
subtree_cnt = [-1]*(n+1) # subtree_cnt 선언

for _ in range(n-1): # n-1번 반복
    u, v = map(int, input().split()) # u, v값 입력받음
    graph[u].append(v) # graph[u]에 v 삽입
    graph[v].append(u) # graph[v]에 u 삽입

tree_dp(r, graph) # 함수 연산


# 출력
for _ in range(q): # q번 반복
    print(subtree_cnt[int(input())]) # 결과 출력
