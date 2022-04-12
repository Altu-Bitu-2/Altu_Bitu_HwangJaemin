import sys # sys 호출
input = sys.stdin.readline # input에 sys.stdin.readline을 대입해서 간결하게 만듬

"""
[저울]
- 작은 값부터 측정 가능한지 파악해야 하므로, 오름차순으로 정렬한다.
- 현재 0부터 scope까지 모든 무게를 빠짐없이 측정가능하다고 했을 때, 새로운 무게는 scope + 1보다 작거나 같아야 한다.
- ex) 현재 1~5까지 측정 가능한데, 다음 값이 7인 경우 -> 6은 측정 불가
- 만약 이 조건을 만족할 경우, 측정 가능한 범위는 [1, scope + 새로운 무게]로 갱신된다.
- 모든 저울을 살펴봤는데도 비어있는 값이 없으면, scope + 1 리턴
3, 1, 6, 2, 7, 30, 1 -> 21
1, 1, 2, 3, 6, 7, 30
"""

def find_unmeasurable(weight): # 측정 불가능한 값을 구하는 함수 구현
    weight.sort()   # 작은 무게부터 측정하도록 리스트를 오름차순으로 정렬
    scope = 0 # 만들 수 있는 무게 중에서 가장 큰 값

    for w in weight: # weight 리스트에 있는 원소들에 대해서
        if scope + 1 < w: # 만약 w가 scope+1(측정할 수 없는 양의 정수 무게 중 최솟값)보다 크다면
            return scope + 1 # scope+1 반환해줌
        scope += w # 그렇지 않으면 scope 값에 weight를 더해줌          

    return scope + 1 # scope+1 반환

n = int(input()) # n값 입력받음
weight = list(map(int, input().split())) # weight 리스트에 입력받은 값 저장

print(find_unmeasurable(weight)) # 함수 결과값 출력
