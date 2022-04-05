import sys # readline 사용을 위해 sys 불러옴
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
[등수 구하기]
1. n = 0일 때, 항상 1 출력
2. 등수는 p보다 작지만, 랭킹 리스트에 들어가지 못하는 경우 고려
.find(value): value가 있는 첫번째 인덱스를 리턴, 없으면 에러 발생
입력된 점수를 기존 리스트에 넣고 인덱스 구하기 -> 해당 점수의 첫번째 인덱스 리턴
.count(value): 리스트에서 value의 수를 세어 리턴, 없으면 에러 발생
전체 점수 중 동점자의 수 구하기 -> 첫번째 등수(인덱스 + 1) + 동점자 수 - 1 
                                = 첫번째 인덱스 + 동점자 수 
                                = 해당 점수의 마지막 등수
마지막 등수가 p를 넘지 않으면, 첫번째 인덱스로 구한 등수가 정답
"""

# 입력
n, new_score, p = map(int, input().split())
# 리스트에 들어있는 점수의 개수, 태수의 새로운 점수, 랭킹 리스트에 올라갈 수 있는 점수 개수가 주어짐

if n == 0: # 리스트에 점수가 하나도 없는 경우
    answer = 1 # 태수가 항상 1등
    
else:
    scores = list(map(int, input().split())) # 리스트에 들어있는 점수들을 입력받음
    
    # 해당 점수의 가장 상위 등수 구하기
    scores.append(new_score) # 기존 리스트에 태수 점수 추가
    scores.sort(reverse=True) # 내림차순으로 정렬
    first_idx = scores.index(new_score) # 리스트에서 태수의 새 점수 인덱스를 찾고 first_idx에 저장

    # 동점자가 몇 명 있는지 구하기
    same_score = scores.count(new_score) # 리스트 내에 태수의 점수와 동일한 점수가 몇 개 있는지 same_score에 저장

    if first_idx + same_score <= p: # 둘을 합친게 랭킹 리스트에 올라갈 수 있는 점수 개수보다 작다면
        answer = first_idx + 1 # 태수의 등수를 answer 변수에 저장(first_idx는 인덱스니까 1을 더해줘야 함)
    else: # 이미 스코어 보드가 다 찬 경우
        answer = -1 # -1 리턴해줌

print(answer) # 정답 출력
