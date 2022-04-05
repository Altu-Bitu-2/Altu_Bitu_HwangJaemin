import sys # readline 사용을 위해 sys 불러옴
from collections import deque # 컨베이어벨트 양 끝에서 로봇이 올라가고 내려가므로 덱 사용
input = sys.stdin.readline # 사용하기 용이하게 input으로 바꿈

"""
 [컨베이어 벨트 위의 로봇 문제]
 1. 벨트가 각 칸 위의 로봇과 함께 한 칸 회전
 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트 회전 방향으로 한 칸 이동할 수 있다면 이동 (이동가능: 이동하려는 칸에 로봇이 없고, 그 칸의 내구도가 1 이상이어야 함)
 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇 올림
 4. 내구도가 0인 칸의 개수가 k개 이상이라면 과정 종료. 그렇지 않다면 1로 돌아감
 [문제 풀이]
 벨트의 회전을 구현하기 위해서 deque 사용
 1번: 벨트를 오른쪽으로 한칸 회전
 2번: 가장 먼저 올라간 로봇부터 고려해야 하므로 (내리는 위치 - 1)부터 (올리는 위치)까지 검사 -> 로봇 옮기는 거 가능하면 존재여부 체크하고 내구도 감소
 3번: 올리는 위치 칸 내구도 0이 아니라면 해당 칸 로봇 존재 여부 체크 + 내구도 감소
"""

def simulation(n, k, belt): # n은 컨베이어 벨트의 길이, 내구도가 0인 칸의 개수가 k개 이상이면 과정 종료.
    size = 2 * n # 벨트 길이
    robots = deque([False] * size)  # 벨트 위에 로봇이 존재하는지 여부 저장
    
    up_idx = 0  # 로봇을 올리는 위치
    down_idx = n-1  # 로봇을 내리는 위치

    step = 0 # 로봇 옮기는 단계
    count = 0   # 내구도가 0인 칸의 수
    
    while True:
        step += 1 # 첫 번째 스텝(벨트가 각 칸 위에 있는 로봇과 함게 한 칸 회전)

        robots.rotate(1) # rotate - 리스트를 회전시키는 내장함수. 로봇을 한 칸 옆으로 이동시킴
        belt.rotate(1) # 벨트를 한 칸 옆으로 이동시킴
        
        robots[down_idx] = False    # 로봇이 내리는 위치에 있다면 내려줌

        # 2. 로봇 이동
        for idx in range(down_idx-1, up_idx-1, -1): #가장 먼저 올라간 로봇부터 고려. (내리는 위치-1)부터 올리는 위치까지 하나씩 감소시켜가면서 반복
            if robots[idx] and not robots[idx + 1] and belt[idx + 1] > 0: # robots[idx]가 True고 robots[idx+1]이 False인 경우
                robots[idx] = False # 로봇이 한 칸 옆으로 이동했으니 idx번째 칸은 비었으므로 False로 바꿔주기
                robots[idx + 1] = True # 한 칸 옆으로 이동해서 현재 있는 칸. 로봇이 있으므로 True로 바꿔주기
                belt[idx + 1] -= 1 # 벨트 내구도 감소
                if belt[idx + 1] == 0: # 벨트의 내구도가 0이 되면
                    count += 1 # 내구도가 0인 칸의 수 하나 증가시킴

        
        robots[down_idx] = False # 내리는 위치까지 도달, 로봇을 내림
        
        # 3. 로봇 올리기
        if belt[up_idx] > 0: # 로봇이 올라가는 부분의 내구도가 0보다 크다면
            robots[up_idx] = True # 로봇을 올림
            belt[up_idx] -= 1 # 올라가는 부분 내구도 1 감소
            if belt[up_idx] == 0: # 내구도가 0이 된다면
                count += 1 # 내구도가 0인 칸의 수 하나 증가

        if count >= k: # 내구도가 0인 칸의 수가 주어진 k와 같아지면
            break # 반복을 멈추고

    return step # 몇 번째 단계에서 멈추었는지 리턴해줌

# 입력
n, k = map(int, input().split()) # 컨베이어 벨트의 길이와 내구도가 0인 칸의 개수를 입력받음
belt = deque(map(int, input().split()))  # 벨트의 내구도를 저장


# 연산 + 출력
print(simulation(n, k, belt)) # 결과 출력
