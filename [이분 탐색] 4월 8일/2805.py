import sys # sys 불러옴
input = sys.stdin.readline # input에 대입해서 길이를 줄임

"""
 [나무 자르기]
 적어도 M미터의 나무를 집에 가져가기 위해서 절단기에 설정할 수 있는 높이의 최댓값은?
 -> 절단기의 높이가 k(임의의 값)일 때, M미터의 나무를 집에 가져갈 수 있는가?
 left: 절단기의 최소 높이 -> 0
 right: 절단기의 최대 높이 -> 주어진 나무 중 가장 높은 나무 높이
"""

def cut_tree(height, tree): # 
    total = 0 # height보다 값이 큰 요소들에 대해 각 길이와 height의 차를 모두 더한 값

    for h in tree: # tree 리스트에 든 원소 h에 대해
        if h <= height: # h가 height보다 작거나 같다면
            return total # total값을 리턴해줌
        total += h - height # total값에 나무의 높이에서 height 값을 뺀 나머지를 total에 더함
    
    return total # total값 리턴

def binary_search(target, tree): # 이진 탐색 함수
    left = 1 # 절단기의 최소 높이(구하기 편하라고 1로 설정)
    right = tree[0] # 절단기의 최대 높이

    while left <= right: # left값이 right보다 작거나 클 동안에
        mid = (left + right) // 2 # mid값은 left값과 right값을 합친 결과의 절반값
        if cut_tree(mid, tree) >= target: # cut_tree 함수의 결과값이 target보다 크다면
            left = mid + 1 # left값에 mid+1 대입
        else: # 그렇지 않다면
            right = mid - 1 # right값에 mid-1 대입

    return left - 1 # left-1값을 리턴해줌

# 입력
n, m = map(int, input().split()) # 나무의 수와 상근이가 필요한 나무의 길이 입력받음
tree = list(map(int, input().split())) # 나무들의 높이 입력받음
tree.sort(reverse=True) # 내림차순 정렬
print(binary_search(m, tree)) # 정답 출력
