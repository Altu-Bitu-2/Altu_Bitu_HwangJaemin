import sys # sys 호출
input = sys.stdin.readline # input에 sys.stdin.readline 대입

"""
[행운의 바퀴]
- 바퀴가 돌아갈 필요 X
- 화살표가 가르키는 인덱스를 회전 정보에 따라 바꿔줌
1. 화살표가 가르키는 칸이 결정되지 않았으면 알파벳을 바퀴에 적는다.
2. 이미 알파벳이 써 있는 경우, 같은 알파벳이 아닌 경우 조건에 해당하는 바퀴 만들 수 없다.
3. 바퀴에 쓰여있는 알파벳은 중복되지 않으므로 동일한 알파벳이 여러 자리에 있을 수 없다.
"""

def make_wheel(n, record): # 바퀴에 적어놓은 알파벳을 알아내기 위한 함수
    wheel = ['?'] * n   # 바퀴의 상태(어떤 숫자가 있는지 모르는 칸은 ?로 표시)
    is_available = dict()   # 해당 알파벳을 새로 쓸 수 있는지 확인하는 딕셔너리

    # chr(아스키코드) = 문자
    ord_a = ord('A') # ord(문자) - 해당 문자의 아스키 코드 구해주는 내장함수
    for i in range(26):
        is_available[chr(i + ord_a)] = True # 모든 알파벳에 대해 True

    idx = 0 # 화살표가 가르키는 인덱스

    for rot, alpha in record: # rot - 화살표가 가리키는 글자가 변하는 횟수, alpha - 회전이 멈추었을 때 가리키고 있는 글자
        idx = (idx - int(rot)) %n # 화살표가 가리키는 인덱스를 회전 정보에 따라 변경해줌
        
        if wheel[idx] == alpha: # idx에 들어있는 알파벳과 회전이 멈추었을 때 화살표가 가리키고 있는 알파벳이 동일할 때
            continue # 다음 코드 계속 수행
        if wheel[idx] != '?' or not is_available[alpha]: # 다른 알파벳이 써 있거나, 이미 알파벳을 다른 자리에 사용한 경우
            return '!' # 해당하는 행운의 바퀴가 없으므로 '!' 출력
        wheel[idx] = alpha # 위의 경우가 아니라면 wheel 리스트의 idx번째 원소에 화살표가 가리키는 알파벳 대입
        is_available[alpha] = False # 한 번 사용되었으므로 이후 같은 알파벳 사용 불가
                
    return ''.join(wheel[idx:]+wheel[:idx]) # wheel 리스트의 idx 원소만 빼고 출력

# 입력
n, k = map(int, input().split()) # 바퀴의 칸 수와 바퀴를 돌리는 횟수 입력받음
record = [input().split() for _ in range(k)] # 종이에 적어놓은 내용 입력받음
     
print(make_wheel(n, record)) # 결과 출력 
