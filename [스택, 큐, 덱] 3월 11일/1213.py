import sys
input = sys.stdin.readline

names = input()
name_cnt = [0 for _ in range(26)]
#입력값의 알파벳 종류와 개수를 세기 위함. 나는 리스트에 A, B, C... 싹 다 넣어야 하나 고민했는데 이런 방법이 많이 나오는 것 같음.
for name in names:
    if ord(name) == 10:
        break
    name_cnt[ord(name)-65] += 1
#ord()함수는 ()안의 아스키 코드값을 반환해줌.

odd = 0
oddA = ''
evenA = ''

for i in range(26):
    if name_cnt[i]%2==1:
        odd+=1
        oddA += chr(i+65)
    evenA += chr(i+65) * (name_cnt[i]//2)
    #좌우대칭이니까 문자열 반만 뚝 잘라서 앞에 붙이고 역순으로 된 걸 뒤에 붙이면 됨.
if odd>1:
    print("I'm Sorry Hansoo")
else:
    print(evenA+oddA+evenA[::-1]) #홀수개 알파벳중 하나를 가운데에 붙임.
