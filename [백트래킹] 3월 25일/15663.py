import sys # readline 사용을 위해 sys 불러옴
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈


"""
 1. 우선 수열을 사전 순으로 증가하는 순서로 출력해야 하므로 주어진 수열을 오름차순 정렬
 2. 이 상태에서 우선, 같은 위치의 수를 또 선택하지 않도록 중복제거 (check 배열 사용)를 해줌
 3. 그 후, 중복되는 "수열"을 거르는 방법은 이전에 선택한 값을 변수에 저장해서, 수열을 만들다 다시 루트 노드로 돌아왔을 때
    이전에 선택한 값과 같은 값이면 넘어가면 됨! -> 어차피 같은 수이므로 같은 과정 반복해서 똑같은 수열이 나올 것
"""

def backtracking(idx, m): # idx와 m을 입력값으로 가지는 함수 생성
    if idx == m: # idx와 m이 같다면
        print(*answer) # 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌                    
        return # 종료

    prev = 0    # 이전에 선택한 값
    for i in range(n): # n번동안 반복
        if not checked[i] and arr[i] != prev: # checked[i]가 False이고 arr[i]의 값이 이전에 선택한 값과 같지 않다면
            checked[i] = True # checked[i]를 True로 바꿔주고
            prev = arr[i] # 이전에 선택한 값이 arr[i]가 됨
            answer[idx] = arr[i] # answer[idx]의 값을 arr[i]값으로 변경
            backtracking(idx + 1, m) # 백트래킹, idx 다음값을 입력값으로 넣음
            checked[i] = False # checked[i]에 False값을 넣어줌

    return # 종료
            
n, m = map(int, input().split()) # n과 m값을 입력받음
arr = list(map(int, input().split())) # 길이가 m인 수열을 입력받음
arr.sort() # arr 리스트 정렬
checked = [False] * n # 중복 제거를 위해 checked 배열 생성
answer = [0] * m # 

backtracking(0, m) # 함수 사용
