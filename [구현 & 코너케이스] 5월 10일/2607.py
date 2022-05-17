
'''
<문제 분석>
두 단어가 같은 구성을 갖거나, 한 단어에서 한 문자를 더하거나, 빼거나, 하나의
문자를 다른 문자로 바꾸어 나머지 한 단어와 같은 구성을 갖게 되는 경우
서로 비슷한 단어라고 한다
주어지는 단어들 중 첫 번째 단어와 비슷한 단어가 몇 개인지 구해야 함


<코드 구조 설계>
- iterable한 객체를 받아서 횟수를 기록하여 Counter 객체로 반환.
    이때 Counter 객체는 유사 dictionary라고 생각할 수 있다.
    주의할 점은, 일반 dictionary와는 다르게 default 값이 0으로 설정되어 있어,
    삽입하지 않은 키 값에 대한 조회가 가능하다.
'''




import sys # sys 불러옴
from collections import Counter # counter 클래스 사용
input = sys.stdin.readline # 가독성을 위해 input에 대입

SIZE = 26 # 알파벳 개수


# 입력
n = int(input()) # 입력받을 단어 개수가 주어짐

source = input().rstrip() # 첫 번째 단어 저장
source_cnt = Counter(source) # 입력받은 단어 중 가장 많이 등장한 순으로 정렬, source_cnt에 저장함
ans = 0 # 비슷한 단어 개수

alphabets = [chr(i + ord('A')) for i in range(SIZE)]    # 알파벳 리스트

for _ in range(n-1): # n-1동안 반복
    target = input().rstrip() # 나머지 단어 입력받음
    diff = 0 # 첫 번째 단어와 다른 부분이 있으면 카운트할 변수
    target_cnt = Counter(target) # 입력받은 단어 가장 많이 등장한 순으로 정렬, target_cnt에 저장

    for key in alphabets: # 알파벳 리스트의 원소 하나하나에 대해서
        diff += abs(target_cnt[key] - source_cnt[key])  # Counter 객체이므로 키가 존재하는지 확인 불필요
    
    if diff <= 1 or (diff == 2 and len(target) == len(source)): # 조건에 맞는다면
        ans += 1 # 비슷한 단어 수 하나 증가시킴
    
print(ans) # 결과값 출력
