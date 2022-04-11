import sys # readline 사용을 위해 sys 불러옴
import heapq # 힙 자료구조를 사용하기 위해 heapq 불러옴 
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
[파일 합치기 3]
- 파일을 전부 합치기 위해서는 어차피 하나로 만들어야 한다!
- 이 때, 여러번 더해지는 값은 작을 수록 좋다
- 따라서, 현재 가장 작은 파일 2개를 합쳐야 비용을 최소화 할 수 있다.
-> 최소 힙으로 구현
"""

def get_cost(pq): # 비용 계산하는 함수 정의 
    heapq.heapify(pq) # pq 리스트를 힙으로 변환
    
    cost = 0 # 파일들을 하나의 파일로 합칠 때 필요한 최소비용
    while len(pq) > 1: # pq에 원소가 들어있다면
        file1 = heapq.heappop(pq) # file1은 pq의 최솟값
        file2 = heapq.heappop(pq) # file2는 file1을 pop한 뒤의 최솟값
        cost += file1 + file2 # 가장 작은 파일 2개를 합쳐 비용을 최소화
        heapq.heappush(pq, file1 + file2) # pq에 file1과 file2를 합친 값 삽입

    return cost # 최소비용 리턴

t = int(input()) # 테스트 데이터 입력

for _ in range(t): # t동안 반복
    n = int(input()) # 1장부터 k장까지 수록한 파일의 크기 입력받음
    files = list(map(int, input().split())) # 리스트 형태의 파일 크기
    print(get_cost(files)) # files 리스트를 대입해 함수 결과(최소 비용) 출력
