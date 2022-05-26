import sys
input = sys.stdin.readline

n = int(input())
nums = int(input())
students = list(map(int, input().split()))

frames = dict()

for i in range(nums):
    if students[i] in frames :
        frames[students[i]][0] += 1
    else:
        if len(frames) < n:
            frames[students[i]] = [1, i]
        else:
            delList = sorted(frames.items(), key = lambda x: (x[1][0], x[1][1]))
            delKey = delList[0][0]
            del(frames[delKey])
            frames[students[i]] = [1, i]
result = list(sorted(frames.keys()))
answer = str(result[0])
for i in result[1:]:
    answer += ' ' + str(i)

print(answer)
