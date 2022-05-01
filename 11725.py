import sys # sys 불러옴 
sys.setrecursionlimit(10**8) # 트리 최대 깊이를 10**8로 설정해줌
input = sys.stdin.readline # input에 대입

"""
[트리의 부모 찾기]
- 1번 노드에서 출발해서 탐색
- 루트 노드에서 출발 했기 때문에, 현재 노드의 부모는 이전 노드가 된다.
- (주의) 트리 노드의 최대 수가 100,000이므로, 가능한 트리의 최대 깊이는 100,000번이 된다. 즉, 재귀 깊이 또한 100,000번이 되므로 재귀 깊이 제한을 재설정 해야한다.
"""

def dfs_recursion(prev, curr): # 트리 부모 찾아주는 함수
    if parent[curr]: parent[curr] # parent[curr]값이 0이 아니라면 parent[curr]값 출력
        return # 리턴
    
    parent[curr] = prev # parent[curr]값에 prev값 대입

    for next in adj_list[curr]: # adj_list[curr]에 들어있는 원소 next에 대해
        dfs_recursion(curr, next) # 재귀함수 수행
    return # 리턴

n = int(input()) # 노드의 개수
adj_list = [list() for _ in range(n+1)] # 빈 리스트 만들어줌
parent = [0] * (n + 1) # 0을 n+1개 가지고 있는parent 리스트 선언

for _ in range(n-1): # n-2번동안 반복
    a, b = map(int, input().split()) # a, b값 입력받음
    adj_list[a].append(b) # adj_list[a]에 b 원소 추가
    adj_list[b].append(a) # adj_list[b]에 a 원소 추가

dfs_recursion(1, 1)   # 1번 노드는 루트노드이므로, 부모를 자기 자신으로 설정
print(*parent[2:], sep='\n') # 정답 출력
