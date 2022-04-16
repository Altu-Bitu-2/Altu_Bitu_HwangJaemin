import sys # sys 호출
from itertools import permutations # itertools를 이용해 순열 구하기
input = sys.stdin.readline # 길이를 줄이기 위해 input에 sys.stdin.readline 대입

"""
[야구]
1. 가능한 모든 배치를 구한다.
    - 이때, 4번 타자는 항상 1번 선수(0번 인덱스)여야 함을 주의
2. 구한 배치에 대해 점수를 계산
    - out이 3번을 기록하여 이닝이 바뀔 때, 이전에 베이스에 있던 선수들을 비워주어야 함
    - 선수 인덱스를 갱신하는 과정에서 인덱스 에러가 나지 않도록 모듈러 연산 해주기
"""

def calc_score(order, result): # 구한 순서에 대해 점수를 계산
    player = 0 # 야구선수
    score = 0 # 현재 점수
 
    for inning in result: # result의 한 행이 inning
        out = 0 # 아웃당한 선수 수 
        base1 = base2 = base3 = 0 # 주자 수
        while out < 3: # 쓰리아웃 전까지
            p = inning[order[player]] # 이번 타자의 포인트
            if p == 0: # 아웃인 경우
                out += 1 # 아웃인 사람 수 증가
            elif p == 1: # 안타인 경우
                score += base3 #3루에 있는 선수가 홈으로 들어와 1점을 얻음
                base3 = base2 # 2루에 있던 선수가 3루로 옴
                base2 = base1 # 1루에 있던 선수가 2루로 옴
                base1 = 1 # 1루에 새로운 선수가 들어옴
            elif p == 2: # 2루타인 경우
                score += base3 + base2 # 홈에 3루와 2루에 있는 선수가 들어옴
                base3 = base1 # 3루에는 1루에 있던 선수가 들어옴
                base2 = 1 # 2루타여서 2루까지 진입
                base1 = 0 # 1루에는 아무도 없음
            elif p == 3: # 3루타인 경우
                score += base3 + base2 + base1 # 1루, 2루, 3루에 있던 선수들이 모두 홈에 들어옴
                base3 = 1 # 3루타여서 3루까지 진입
                base2 = base1 = 0 # 2루와 1루에는 아무도 없음
            else: # 홈런인 경우
                score += base3 + base2 + base1 + 1 #타자와 모든 주자가 홈까지 진루
                base3 = base2 = base1 = 0 # 1루, 2루, 3루에 아무도 없음
            # 다음 타자로 바꿔 줌
            player = (player + 1) % 9 # 인덱스 갱신 과정에서 에러가 나지 않도록 모듈러 연산                       

    return score # 최종 점수 반환


# 입력
n = int(input()) # 이닝 수 입력받음
result = [list(map(int, input().split())) for _ in range(n)]    # 각 이닝별 득점결과
answer = 0 # 결과값


for order in permutations(range(1, 9), 8): # 가능한 모든 배치를 구하되, 1번타자(0번 인덱스)는 고정되어 있음을 주의
    order = list(order) # 구한 순열을 리스트로 만듬
    order.insert(3, 0) # 리스트 네 번째 요소에 0 삽입
    # 최댓값 갱신
    answer = max(answer, calc_score(order, result)) # answer과 함수로 구한 최종 점수 중에 더 큰 쪽을 answer에 저장

print(answer) # answer 출력
