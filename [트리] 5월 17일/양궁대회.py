SIZE = 10 # k점(1~10점 사이)

"""
 [양궁대회]
 1. 가능한 모든 경우를 백트래킹 탐색을 통해 검사
 -> 라이언이 점수를 얻어가려면 어피치보다 1개 더 쏘는 경우가 최적. 어피치보다 적게 화살 쏘는 건 점수 못 얻어가므로 어차피 의미가 없음.
 -> 따라서 라이언이 각 점수에 화살을 아래와 같이 쏘는 2가지 경우만 고려해서 만들어지는 모든 경우를 백트래킹으로 탐색
    - 어피치가 점수 획득을 하는 경우: 해당 점수에는 화살을 한 발도 쏘지 않는 것이 이득
    - 라이언이 점수 획득을 하는 경우: 필요한 최소 화살을 사용하는 것이 이득이므로 어피치보다 정확히 한 발 더 쏨
 !주의! 0번 인덱스가 10점 과녁임을 주의
"""

max_diff = 1 # 라이언과 어피치 점수 차 최댓값
answer = [-1] # 출력할 정답값(-1만 저장)


def backtracking(idx, left, diff, ryan, appeach): # 백트래킹 함수 정의
    global max_diff, answer # 전역변수 선언
    # 기저조건 - 0점 과녁까지 모두 탐색한 경우
    if idx == SIZE: # idx와 SIZE값이 같다면
        ryan[idx] = left # ryan의 idx번째 원소가 left와 동일하다면
        
        if diff > max_diff: # 라이언과 어피치 점수 차가 최대 점수차 값보다 크다면
            max_diff = diff # 최대 점수차 업데이트
            answer = ryan[:] # answer에 라이언 리스트 원소들 저장
        elif diff == max_diff: # 라이언과 어피치 점수차가 최대 점수차 값과 같다면
            if ryan[::-1] > answer[::-1]: # 라이언 점수가 저장된 리스트의 역이 answer 리스트 역보다 크다면
                answer = ryan[:] # answer 리스트에 라이언 점수 리스트 대입
        return # 리턴해줌
    
    # 남은 화살로 라이언이 점수를 얻을 수 있는 경우
    if left > appeach[idx]: # 남은 화살이 어피치가 10-idx점 과녁에 맞힌 개수보다 크다면 
        ryan[idx] = appeach[idx] + 1 # 라이언이 10-idx점 과녁에 맞힌 화살 개수는 어피치가 맞힌 개수+1
        backtracking(idx+1, left - ryan[idx], diff + SIZE - idx, ryan, appeach) # 백트래킹 사용
        ryan[idx] = 0 # idx번째 점수 0으로 초기화

    # 어피치가 점수를 얻을 수 있는 경우 점수 계산
    if appeach[idx]: # idx번째 원소가 있다면
        diff -= SIZE - idx # diff값에서 SIZE-idx값을 빼줌
    backtracking(idx+1, left, diff, ryan, appeach) # 백트래킹 사용
    return # 리턴해줌

def solution(n, info): # 정답을 출력해주는 함수
    ryan = [0]*11   # 라이언 과녁 정보
    backtracking(0, n, 0, ryan, info) # 백트래킹 사용
    
    return answer # answer값 리턴


# 디버깅 위한 메인 코드 - 프로그래머스에는 제출 X
if __name__ == "__main__": # 프로그램을 실행하면
    n = 5 # n에 5값 대입
    info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0] # 어피치의 점수

    print(*solution(n, info)) # 정답 출력
