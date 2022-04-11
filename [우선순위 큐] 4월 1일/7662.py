import sys # readline 사용을 위해 sys 불러옴
import heapq as hq # 힙 자료구조를 사용하기 위해 heapq를 hq로 불러옴
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
[이중 우선순위 큐]
최대 힙과 최소 힙 두가지로 나누어 저장
다른 힙에서 이미 제거된 값을 판단하기 위해, 큐에 값이 들어올 때마다 is_valid에 상태를 저장한다.
만약 최대 힙/최소 힙에서 값을 꺼냈을 때 해당 인덱스의 is_valid 원소가 False로 표기되어 있다면, 이미 다른 큐를 통해 제거된 값이므로 버리고 다시 꺼내야 한다.
"""

testcase = int(input()) # 테스트 케이스를 입력받음 

def remove_invalid_data(heap): # 힙에서 유효하지 않은 값은 삭제해줌
    while heap and not is_valid[heap[0][1]]: #힙이 비어있지 않고 top이 invalid하면 
        hq.heappop(heap) # pop해줌
    return # 힙이 비어있고 top이 valid하다면 함수 종료

for _ in range(testcase): # 테스트케이스만큼 반복해서
    t = int(input()) # 입력 데이터의 수 t를 입력받음

    max_heap = list() # 최대힙을 리스트 형태로 만듬
    min_heap = list() # 최소힙을 리스트 형태로 만듬
    is_valid = list() # 값의 유효성을 저장할 리스트를 만듬
    idx = 0     # 이번에 들어올 값의 인덱스
                # is_valid[idx]에 값의 유효성이 저장된다.
    
    for _ in range(t): # t만큼 반복해서
        cmd, n = input().split() # 연산을 나타내는 문자와 정수 n을 입력받음
        if cmd == 'D': # 커맨드가 D(삭제)이고
            if int(n) == 1: # 정수 n이 1이라면
                remove_invalid_data(max_heap) # 최대힙에서 유효하지 않은 값을 삭제함
                if max_heap: # 최대힙이 비어있지 않다면        
                    is_valid[hq.heappop(max_heap)[1]] = False # 값을 제거한 후에 유효성을 갱신
            else: # 이외의 경우
                remove_invalid_data(min_heap) # 최소힙에서 유효하지 않은 값을 삭제함
                if min_heap: # 최소힙이 비어있지 않다면 
                    is_valid[hq.heappop(min_heap)[1]] = False # 값을 제거한 후에 유효성을 갱신
        else: # 커맨드가 D가 아닌 경우
            hq.heappush(max_heap, (-int(n), idx)) # 최대힙에 -n과 인덱스 저장
            hq.heappush(min_heap, (int(n), idx)) # 최소힙에 n과 인덱스 저장
            is_valid.append(True)   # 우선 유효하다고 저장
            idx += 1 # 인덱스 값을 하나 더해줌

    remove_invalid_data(max_heap) # 최대힙에 유효하지 않은 값이 top에 있으면 제거
    remove_invalid_data(min_heap) # 최소힙에 유효하지 않은 값이 top에 있으면 제거

    if max_heap: # 최대힙에 원소가 들어있다면
        print(-max_heap[0][0], min_heap[0][0]) # Q에 남아 있는 값 중 최댓값과 최솟값(최대힙과 최소힙의 루트) 출력
    else: # 최대힙에 원소가 없다면
        print("EMPTY") # EMPTY 출력
