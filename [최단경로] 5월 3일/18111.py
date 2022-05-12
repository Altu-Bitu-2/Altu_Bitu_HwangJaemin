import sys # sys 불러옴
input = sys.stdin.readline # 가독성을 위해서 input에 대입

INF = 10**9 # INF값 설정

"""
[마인크래프트]
 1. 가장 낮은 땅의 높이를 h라고 할 때, h-1의 높이를 만드는건 h보다 2*(N*M)의 시간이 더 소요됨
 2. 가장 높은 땅의 높이를 h라고 할 때, h+1의 높이를 만드는건 h보다 (N*M)의 시간이 더 소요됨
 -> 따라서 땅의 높이가 될 수 있는 후보는 (가장 낮은 땅) ~ (가장 높은 땅)
 -> 위치에 관계없이, 높이에 따라 필요한 블록 수와 시간이 결정되기 때문에 해당 높이의 블록이 몇 개 있는지 미리 저장 -> 가능한 높이 당 최대 256번의 연산만으로 계산 가능
 !주의! 당장 쌓을 블록이 없더라도 언젠가 다른 곳의 블록을 제거해서 쌓을 수 있음.
"""

def mine_land(min_height, max_height, b, height, cnt): # 함수 정의
    t = 0 # t값 초기화
    for i in range(min_height, height): # mine_height값부터 height-1값이 될때까지 반복
        temp = cnt[i] * (height - i) # temp에 cnt[i]*(height - i)값 대입
        b -= temp # 블록 수에서 temp만큼 빼줌
        t += temp # t값에 temp만큼 더해줌

    for i in range(height, max_height + 1): # height값부터 max_height값이 될 때까지 반복
        temp = cnt[i] * (i - height) # temp에 cnt[i]*(i-height)값 대입
        b += temp # 블록 수에서 temp만큼 더해줌
        t += temp * 2 # t값에 temp*2값만큼 더해줌

    if b < 0: # b가 음수라면
        return INF + 1 # INF+1값 리턴

    return t # t값 리턴


# 입력
n, m, b = map(int, input().split()) # n, m, b값 입력받음

cnt = [0]*257   # cnt[i] = 높이 i를 가지고 있는 땅의 수
min_height = 256 # 최소 높이값
max_height = 0 # 최대 높이값

for _ in range(n): # n동안 반복
    for i in map(int, input().split()): # 입력값을 받아서 반복
        cnt[i] += 1 # cnt[i]값에 1 더해줌
        min_height = min(min_height, i) # min_height와 i값중 더 작은 쪽을 min_height에 대입
        max_height = max(max_height, i) # max_height와 i값중 더 큰 쪽을 max_height에 대입

min_t = INF # min_t값에 INF값 대입
height = 0 # height값 대입

# 연산
for h in range(min_height, max_height+1): # min_height부터 max_height가 될때까지
    t = mine_land(min_height, max_height, b, h, cnt) # t값에 함수 결과값 대입
    if t <= min_t: # t값이 min_t값보다 작거나 같다면
        min_t = t # min_t값에 t값 대입
        height = h # height값은 h값 대입

# 출력
print(min_t, height) # 결과 출력
