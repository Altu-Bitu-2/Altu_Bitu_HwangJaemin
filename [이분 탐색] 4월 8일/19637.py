import sys # sys 불러옴
from bisect import bisect_left # bisect의 bisect_left를 사용해서 정렬된 순서를 유지하면서 리스트에 데이터를 삽입할 가장 왼쪽 인덱스를 찾음
input = sys.stdin.readline # input에 sys.stdin.readline 대입해서 길이 줄이기

"""
 [IF문 좀 대신 써줘]
 모든 캐릭터와 칭호를 매칭하는 브루트 포스를 사용하기엔 최대 연산 횟수 10^5 * 10^5 -> 100억!
 특정 전투력 '이하'까지 해당하는 칭호를 받을 수 있음
 -> 이분 탐색
"""

# 입력
n, m = map(int, input().split()) # 칭호의 개수와 캐릭터의 개수 입력받음
names = [] # 칭호명 목록
power = [] # 칭호의 기준이 되는 전투력 상한값

# 이미 능력치에 대한 오름차순으로 입력되므로 정렬 필요 X
for _ in range(n): # n번동안 반복
    name, p = input().split() # 칭호 이름과 전투력 입력받음
    names.append(name) # 이름을 names 리스트에 추가
    power.append(int(p)) # 전투력을 power 리스트에 추가

for _ in range(m): # m번동안 반복
    print(names[bisect_left(power, int(input()))]) # 리턴 받은 인덱스로 name을 조회(찾기만 하고 power 리스트에 입력받은 전투력을 저장하는건 아님)
