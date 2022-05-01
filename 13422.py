import sys # sys 불러오기
input = sys.stdin.readline # 편의를 위해 input에 대입

"""
 [도둑]
 1. 연속해서 훔쳐야 할 집이 m으로 고정됐기 때문에 슬라이딩 윈도우
 2. 직선이 아니라 원 형태의 배열! 모듈러 연산을 통해 윈도우의 양 끝 위치 조절하기
 !주의! 마을에 있는 집의 개수와 도둑이 훔칠 집의 개수가 같을 때(n==m) 도둑이 훔칠 수 있는 경우의 수 1개!
    => 예를 들어, n = m = 3, k = 4, house = [1, 1, 1] 일 때, 실제 방법의 수는 1번, 2번, 3번 집을 택하는 경우밖에 없지만
       예외 처리를 안해줄 경우, 원형으로 돌며 3을 출력하게 됨!
"""

def steal(n, m, k, house): # 돈을 훔칠 m개의 연속된 집을 고르는 방법의 수 계산하는 함수
    # 윈도우 초기화
    money = sum(house[:m]) # 0~m-1번째 집이 가지고 있는 돈의 합
    count = 0 # 돈 훔치는 가짓수

    if money < k: # 방범 장치가 울리지 않는 액수일 때
        count += 1 # 가짓수 + 1

    if n == m: # 마을에 있는 집의 개수와 연속된 집의 수가 같다면
        return count # count값 리턴해줌

    for i in range(m, n + m -1): # i에 m부터 n+m-2까지의 값을 대입하며 반복
        money -= house[i - m] # 돈의 합에서 i-m번째 집이 가진 돈의 액수를 빼줌
        money += house[i % n] # 돈의 합에서 i%n번째 집이 가진 돈의 액수를 더해줌

        if money < k: # 돈의 합이 방범 장치가 울리지 않는 액수이면
            count += 1 # 가짓수+ 1
        
    
    return count # 돈 훔치는 가짓수 출력

# 입력
t = int(input()) # 테스트 케이스 개수

for _ in range(t): # t번 반복
    # 입력
    n, m, k = map(int, input().split()) # 마을에 있는 집의 개수, 도둑이 돈을 훔칠 연속된 집의 개수, 자동 방범 장치가 작동하는 돈의 최소 액수 입력받음
    house = list(map(int, input().split())) # 돈의 양 입력받음
    # 연산 + 출력
    print(steal(n, m, k, house)) # 결과 출력
