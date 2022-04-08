import sys # readline 사용을 위해 sys 불러옴
sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
[연산자 끼워넣기]
연산자를 모두 돌려보면서 배치한 후, 각 연산자에 따른 값 계산
"""

MAX = 10**9 #'연산자를 어떻게 끼워넣어도 항상 10억보다 작거나 같은 결과가 나오는 입력만 주어진다.'

add = lambda x, y: x + y # 더하기 람다 함수
sub = lambda x, y: x - y # 빼기 람다 함수
multiply = lambda x, y: x * y # 곱하기 람다 함수

# C++14 방식에 맞추어 나누기 함수 작성
def division(x, y): # 나눗셈 함수(음수를 양수로 나누는 경우 때문에 람다 함수로 만드는게 불가)
    if x < 0: #음수를 양수로 나눌 경우
        return - (-x // y) # 음수를 양수로 바꾼 뒤 몫을 취하고, 그 몫을 음수로 바꿈
    return x // y # 이외의 경우는 일반적인 나눗셈 출력

functions = [add, sub, multiply, division] # 위에서 만든 함수를 리스트에 저장

# cnt: 수 인덱스, value: 현재까지 연산 결과
def backtracking(cnt, value): # 수 인덱스와 현재까지 연산 결과를 입력값으로 받는 함수
    global max_value, min_value # 최댓값과 최솟값을 전역변수로 선언
    if cnt == n:    # 연산이 모두 완료 되었다면
        max_value = max(max_value, value) # 현재 최댓값과 현재까지의 연산 결과를 비교해서 더 큰 쪽을 새로운 최댓값으로 저장
        min_value = min(min_value, value) # 현재 최솟값과 현재까지의 연산 결과를 비교해서 더 작은 쪽을 새로운 최솟값으로 저장
        return # 연산 종료

    for i in range(4): # 덧셈, 뺄셈, 곱셈, 나눗셈 네 가지라 4번 반복
        if operator[i] > 0: # 연산을 한 번이라도 해야 한다면
            operator[i] -= 1 # 하나식 감소시키고(연산을 할거니까)
            backtracking(cnt + 1, functions[i](value, numbers[cnt]))    # i번째 함수에 value와 numbers[cnt]를 인자로 넘겨주어 계산함
            operator[i] += 1 # 다시 +1 시켜줌
    return

# 입력
n = int(input()) # 수의 개수 입력받음
numbers = list(map(int, input().split())) # 수열 입력받음
operator = list(map(int, input().split())) # 연산자 개수 입력받음

max_value = -MAX   # 현재까지 최대값 기록
min_value = MAX    # 현재까지 최솟값 기록


backtracking(1, numbers[0]) # 함수 사용
print(max_value, min_value, sep='\n') # 결과 출력





