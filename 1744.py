import sys # sys 모듈 불러오기
input = sys.stdin.readline # input에 대입

"""
[수 묶기]
1. 양수는 양수끼리, 음수는 음수끼리 곱해야 큰 수를 만들 수 있다.
2. 절댓값이 큰 것끼리 곱해야 더 큰 수를 만들 수 있다.
     ex) 1, 2, 3, 4 => 4 * 1 + 3 * 2 = 10
                    => 4 * 3 + 2 * 1 = 14
3. 1은 곱하는 것보다 더해야 큰 수를 만들 수 있다. (x * 1 = x < x + 1)
"""

def tie_number(arr): # 수 묶는 함수
    total = 0 # 결과값 저장할 변수
    size = len(arr) # size에 배열 크기 대입
    for i in range(0, size - 1, 2): # 0부터 1까지 size-1씩 증가하는 i에 대해
        total += arr[i] * arr[i + 1] # 결과값에 묶은 수의 곱을 더해줌
    if size % 2: # 수가 짝수개가 아니라면
        total += arr[-1] # 나머지는 그냥 더해줌

    return total # 결과값 리턴

n = int(input()) # 수열 길이 입력받음
arr1 = [] # 1보다 큰 수를 저장
arr2 = [] # 1보다 작은 수를 저장
cnt = 0 # 1의 개수를 저장

for _ in range(n): # n번 반복
    x = int(input()) # 수열에 들어있는 수 입력받음
    if x > 1: # 양수인 경우
        arr1.append(x) # arr1 리스트에 집어넣음
    elif x < 1: # 음수인 경우
        arr2.append(x) # arr2 리스트에 집어넣음
    else: # 0인 경우
        cnt += 1 # cnt값 1 증가

arr1.sort(reverse=True) # 절댓값이 큰 순으로 정렬, 양수이므로 reverse 정렬
arr2.sort() # 절댓값이 큰 순으로 정렬, 음수이므로 sort()만 하면 됨

print(cnt + tie_number(arr1) + tie_number(arr2)) # 결과값 출력
