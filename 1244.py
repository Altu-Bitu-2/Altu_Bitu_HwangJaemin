import sys
input = sys.stdin.readline

"""
[스위치 켜고 끄기]
 남학생 -> 해당 번호의 배수에 해당하는 스위치 상태 바꾸기
 여학생 -> 해당 번호를 중심으로 좌우 대칭이면서 가장 많은 스위치 포함하는 구간의 상태 모두 바꾸기
 좌우 대칭 검사 시, 스위치 범위 주의 (주어진 스위치 범위 넘어가지 않도록)
 스위치 20개씩 출력하는 부분 주의
 인덱스 번호 주의
"""

def change_switch_boy(k, n, switch): # 남학생의 스위치 변경 함수
    # k-1 부터 -> 인덱스는 0부터니까
    for i in range(k-1, n, k): # 인덱스가 0부터니까 for문은 k-1부터 시작
        switch[i] = 1 - switch[i] # i번째 스위치 끄기
    return # 함수 종료


def change_switch_girl(k, n, switch): # 여학생의 스위치 변경 함수
    k -= 1  # k값을 먼저 1 감소시킴
    idx = 0 # 인덱스는 0부터
    while k-idx >= 0 and k+idx < n and switch[k-idx] == switch[k+idx]:  # 스위치 범위가 넘어가거나 좌우 대칭이 깨질 때가지
        switch[k-idx] = switch[k+idx] = 1 - switch[k+idx] # 좌우 대칭이면서 가장 많은 스위치를 포함하는 구간에 속한 스위치 상태를 모두 바꿈
        idx += 1 # idx값 1 증가
    return # 함수 종료

# 입력
n = int(input()) # 스위치 개수 입력받음
switch = list(map(int, input().split())) # 스위치 상태 입력받음
k = int(input()) # 학생 수 입력받음

for _ in range(k): # 학생 수만큼 반복
    a, b = map(int, input().split()) # 학생의 성별, 학생이 받은 수 입력
    if a == 1: # 성별이 1(남자)라면
        change_switch_boy(b, n, switch) # 남학생의 스위치 변경 함수 적용
    else: # 성별이 2(여자)라면
        change_switch_girl(b, n, switch) # 여학생의 스위치 변경 함수 적용

for i in range(0, n, 20): # 한 줄에 20개씩 출력
    print(*switch[i:i+20]) # 결과 출력
