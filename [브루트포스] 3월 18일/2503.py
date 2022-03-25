#2503번
#0은 사용하지 않는다는 걸 주의


n = int(input())

array = []
answer = []

for i in range(123, 1000): #민혁이가 물을 수 있는 수는 123부터(서로 다른 숫자 세 개로 구성)
    temp = str(i)
    if '0' in temp: #0 들어간 수들은 패스
        pass
    elif len(list(set(temp))) == 3: #중복 제거했는데도 여전히 길이가 3이면 조건 만족
        array.append(list(temp))
        answer.append(list(temp))
        
for t in range(n):
    check_number, check_strike, check_ball = map(int, input().split())
    check_number = str(check_number)
    if len(array) == 1:
        continue
        
    for number in array:
        strike = 0; ball = 0
        List = list(check_number)
        for i in range(3):
            if number[i] == check_number[i]:
                List.remove(number[i])
                strike += 1
        ball += len(set(List) & set(number))
        
        if check_strike == strike and check_ball == ball:
            continue
        else:
            if number in answer:
                answer.remove(number)
            else: pass
            
print(len(answer))
