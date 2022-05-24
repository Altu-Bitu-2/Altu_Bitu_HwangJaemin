import sys # sys 불러오기
sys.setrecursionlimit(10**6) # 재귀 최대 깊이 설정

"""
 Ver2. 트리를 직접 작성하지 않고, 바로바로 출력하는 풀이
 전위순회 - V L R
 후위순회 - L R V
 1. 전위 순회는 root 노드의 위치는 알 수 있지만 왼쪽, 오른쪽 서브트리의 경계는 알 수 없음
 2. BST의 성질 : 왼쪽 서브트리의 모든 노드 값 < 루트 노드 값 < 오른쪽 서브트리의 모든 노드 값
    -> 처음으로 root 보다 값이 커진다면, 그 위치가 왼쪽, 오른쪽 서브트리의 경계
 3. 재귀함수 호출로 분할 반복하며 출력
"""

def preorder_to_postorder(start, end): # 전위 순회 -> 후위 순회 함수
    if start > end: # start값이 end보다 큰 경우
        return # 리턴해줌

    curr = preorder[start] # curr에 preorder[start]값 대입

    # 오른쪽 자식이 없는 경우를 미리 확인하여 불필요한 탐색을 줄임
    if preorder[end] <= curr: # 전위 순회 end값이 curr보다 작거나 같다면
        idx = end + 1 # idx값에 end+1 대입
    else: # 그 이외의 경우
        # 오른쪽 자식이 시작되는 인덱스 찾기
        for i in range(start+1, end+1): # start+1 부터 end까지 i값을 하나씩 증가시키면서
            if preorder[i] > curr: # preorder[i]값이 curr값보다 크다면
                idx = i # idx값에 i 대입
                break # 브레이크

    preorder_to_postorder(start + 1, idx-1) # 왼쪽 서브 트리
    preorder_to_postorder(idx, end) # 오른쪽 서브 트리
    postorder.append(curr) # 후위 순회값에 curr 추가

# 입력 & 연산
preorder = [int(i) for i in sys.stdin] # 전위 순회값 입력받음
postorder = [] # 후위 순회 저장할 리스트

preorder_to_postorder(0, len(preorder)-1) # 함수 사용
print(*postorder) # 후위 순회 원소 출력
