import sys # sys 불러옴 
input = sys.stdin.readline # 가독성을 위해서 input에 대입

"""
 [트리]
 기존 리프 노드 개수를 세는 dfs 탐색에서 지우는 정점을 만나면 더 이상 탐색하지 않고 0을 리턴
 !주의! 지우는 정점이 해당 부모 노드의 유일한 자식 노드였을 경우, 해당 정점을 지우면 부모 노드가 리프 노드가 돼서 개수가 1 증가함을 주의
 !주의! 루트 노드가 항상 0이 아님을 주의
"""


def erase_leaf_cnt(node, erase_node): #주어진 정점을 지웠을 때의 리프 노드의 수를 구하는 함수 
    if node == erase_node: # 지워야 할 정점이 루트노드일 때 
        return 0 # 0을 리턴
    if not tree[node] or (len(tree[node]) == 1 and tree[node][0] == erase_node): # tree[node]값이 없거나 tree[node]값이 1이고 tree[node][0] 값이 erase_node와 같을 때
        return 1 # 1을 리턴
    
    cnt = 0 # 리프 노드의 개수 저장할 변수

    for i in range(len(tree[node])): # 0부터 len(tree[node])-1 까지 1씩 증가하는 i에 대해서
        cnt += erase_leaf_cnt(tree[node][i], erase_node) # 함수 리턴값을 cnt에 더해줌
    
    return cnt # cnt값 리턴


# 입력
n = int(input()) # 노드의 개수 입력받음 
tree = [list() for _ in range(n)] # 트리 입력받음

for idx, x in enumerate(input().split()): # enumerate()함수 사용해서 튜플 생성
    if x == "-1": # x값이 -1이면
        root = idx # root값에 idx 대입
    else: # 그렇지 않은 경우
        tree[int(x)].append(idx) # tree[int(x)]에 idx값 넣기

erase_node = int(input())

# 연산 & 출력
print(erase_leaf_cnt(root, erase_node))
