import sys # sys 불러옴
input = sys.stdin.readline # input에 sys.stdin.readline 대입

"""
 [과자 나눠주기]
 n개의 과자가 있을 때 m명의 조카에게 각각 같은 길이로 줄 수 있는 과자의 최대 길이를 구하는 문제
 -> 특정 과자 길이에 대하여 m명의 조카에게 나누어 줄 수 있는가?
 left: 과자 길이의 최솟값 -> 1
 right: 과자 길이의 최댓값
"""

# 내림차순 정렬된 snacks 리스트에서 length 길이의 과자를 몇개 만들 수 있는지 개수를 세어 리턴하는 함수
def split_snack(length, snacks): # 과자 나누는 함수
    count = 0 # 나눠줄 수 있는 아이들의 수 
    for l in snacks: # 과자의 길이에 대해서
        if l < length: # 과자의 길이가 length보다 짧다면
            return count # count 출력
        count += l // length # count에 l//length 더해줌

    return count # count 출력

def binary_search(m, snacks): # 이진탐색 함수
    left = 1 # 과자 길이의 최솟값
    right = snacks[0] # 과자 길이의 최댓값
    while left <= right: # left가 right보다 작다면
        mid = (left + right) // 2 # mid는 left와 right의 평균값
        if split_snack(mid, snacks) >= m: # 나눠줄 수 있는 아이의 수가 m(나눠줘야 하는 아이의 수)보다 크거나 같다면
            left = mid + 1 # left에 mid+1 대입
        else: # 이외의 경우
            right = mid - 1 # right에 mid-1 대입
    return left - 1 # left-1 리턴해줌

m, n = map(int, input().split()) # 조카와 과자 수 입력받음
snacks = list(map(int, input().split())) # 과자 n개의 길이
snacks.sort(reverse=True)   # 내림차순 정렬

print(binary_search(m, snacks)) # 결과 출력 
