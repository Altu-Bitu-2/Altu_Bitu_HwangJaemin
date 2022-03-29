#리스트에 단어 알파벳 입력받기
#이전 단어와 현재 받은 단어가 다를 경우에
#현재 받은 단어가 전전까지 받은 리스트에 들어있는지 검사
#들어있으면 그룹 단어 아님

n = int(input())

for i in range(n):
    words = input().rstrip()
    for t in range(len(words)-1):
        if words[t] != words[t+1]:
            if words[t] in words[t+1:]:
                n-=1
                break
            else:
                pass

print(n)
