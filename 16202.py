import sys # sys 모듈 불러옴
input = sys.stdin.readline # 가독성을 위해서 input에 대입

"""
[MST 게임]
 MST 알고리즘을 여러 번 실행해도 될까?
 1. 크루스칼 알고리즘의 시간 복잡도는 O(ElogE)
    이는 오직 간선을 정렬하는 연산의 시간 복잡도!
    즉, 모든 간선을 한 번 정렬해서 저장해두면 이후 몇 번의 알고리즘을 수행하여도 연산 시간에 큰 영향이 없음
 2. 간선 재사용을 위해 우선순위 큐가 아닌 배열에 저장하고 크루스칼 알고리즘 k번 실행
 3. 매번 크루스칼을 수행할 때마다 제일 먼저 추가한 간선을 제외함
    -> 첫번째 간선은 모든 점이 분리된 상태에서 들어오기 때문에 무조건 사용하게 되어 있고, 이는 사용한 간선 중 가장 짧은 간선
    -> 제외될 간선은 배열의 첫번째 간선부터 순차적 제외
 4. 만약 한 번 MST를 만들 수 없다는게 확인됐다면 이후에도 MST를 만들 수 없음
"""

def find_parent(x): # find 연산
    if parent[x] < 0: # parent[x]값이 0보다 작다면
        return x # x값 리턴
    
    parent[x] = find_parent(parent[x]) # parent[x]에 find_parent(parent[x])값 대입
    return parent[x] # parent[x]값을 리턴

def union(x, y): # union 연산
    px = find_parent(x) # px에 find_parent(x)값 대입
    py = find_parent(y) # py에 find_parent(y)값 대입

    if px == py: # px값과 py값이 같다면
        return False # False 리턴
    
    if parent[px] < parent[py]: # parent[px]값이 parent[py]값보다 작다면
        parent[px] += parent[py] # parent[px]값에 parent[py]값 더해줌
        parent[py] = px # parent[py]값에 px 대입
    else: # parent[px]값이 parent[py]값보다 큰 경우
        parent[py] += parent[px] # parent[py]값에 parent[px]값 더해줌
        parent[px] = py # parent[px]값에 py값 대입

    return True # True값 리턴

def kruskal(n, m, edge, turn): # 크루스칼 함수 정의
    cost = 0 # cost 값 초기화
    cnt = 0 # cnt(증가시켜가면서 턴수와 비교할 것)값 초기화
    for w in range(turn, m+1):
        u, v = edge[w] # u, v에 edge[w]값 대입
        if not union(u, v): # union(u, v)값이 True라면
            continue # 계속

        cost += w # cost값에 w 더함
        cnt += 1 # cnt값 1 증가

        if cnt == n-1: # cnt값이 n-1이라면
            return cost # cost값 리턴해주고 프로그램 종료

    return 0 # 0 리턴해주고 프로그램 종료

n, m, k = map(int, input().split()) # n, m, k값 입력받음

edge = [None] + [tuple(map(int, input().split())) for _ in range(m)] # 간선 정보 입력받음

result = [] # 결과값 저장용 

for turn in range(1, k+1): # 1부터 k까지 1씩 증가하는 turn에 대하여
    parent = [-1]*(n+1) # 초기화
    result.append(kruskal(n, m, edge, turn)) # 연산

    if result[-1] == 0: # 이후의 턴은 모두 0점이므로
        break # 반복문 종료

result += [0]*(k-len(result)) # result값에 더해줌

print(*result) # 결과 출력 
