import sys # sys 호출
input = sys.stdin.readline # 가독성을 위해 input에 대입

"""
[도시 분할 계획]
마을을 두개로 분리하고, 각 집끼리 이동할 수 있는 최소한의 도로만 남기는 문제
즉, 2개의 최소신장트리를 만들어야 하는 문제
-> 하나의 최소신장트리를 만들고, 그 중 가장 유지비가 큰 도로를 삭제
-> 크루스칼 알고리즘에서 가장 마지막에 삭제되는 도로가 유지비가 가장 큼
-> 크루스칼 알고리즘에서 간선을 n-2개만 선택하여 그 합을 구하여 해결
"""

def find_parent(x): # find 연산
    if parent[x] < 0: # parent[x]값이 0보다 작으면 
        return x # x값 리턴해줌
    
    parent[x] = find_parent(parent[x]) # parent[x]에 find_parent(parent[x])값 대입
    return parent[x] # parent[x]값 리턴

def union(x, y): # union 연산
    px = find_parent(x) # px에 find_parent(x)값 대입
    py = find_parent(y) # py에 find_parent(y)값 대입

    if px == py: # px값과 py값이 같다면
        return False # False 리턴
    
    if parent[px] < parent[py]: # parent[px]값이 parent[py]값보다 작다면
        parent[px] += parent[py] # parent[px]값에 parent[py]값 더해줌
        parent[py] = px # parent[py]값에 px 대입
    else: # 그렇지 않은 경우(parent[px]값이 parent[py]값보다 크거나 같은 경우)
        parent[py] += parent[px] # parent[py]값에 parent[px]값 더해줌
        parent[px] = py # parent[px]값에 py 대입

    return True # True 리턴

def kruskal(n, edge): # 크루스칼 알고리즘
    cost = 0 # 유지비용 
    cnt = 0 # 계산 횟수를 세기 위한 변수
    for u, v, w in edge: # 길의 정보를 담은 리스트의 원소에 대해
        if not union(u, v): # union(u, v) 값이 False라면
            continue # 이후 프로그램 계속

        cost += w # cost값에 w를 더해줌
        cnt += 1 # 계산 횟수 1 증가

        if cnt == n-1: # 계산 횟수가 n-1과 동일해졌다면
            return cost # cost값 리턴해줌

    return 0 # 조건 만족하는 경우가 없다면 0 리턴


n, m = map(int, input().split()) # 집의 개수, 길의 개수 입력받음

edge = [tuple(map(int, input().split())) for _ in range(m)] # 길의 정보 입력받음

parent = [-1]*(n+1) # 초기화
 
edge.sort(key=lambda x:x[2])  # 정렬

print(kruskal(n-1, edge)) # 결과 출력
