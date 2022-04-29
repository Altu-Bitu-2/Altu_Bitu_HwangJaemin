import sys
input = sys.stdin.readline

n = int(input())
liquids = list(map(int, input().split()))
liquids.sort()
result = 4e9+1 # 최댓값 설정할때 조심
answer = []

for i in range(n-2):
    fixed = liquids[i]
    left = i + 1
    right = n-1
    while (left < right):
        total = fixed + liquids[left] + liquids[right]

        if abs(total) <= abs(result):
            answer = [fixed, liquids[left], liquids[right]]
            result = total

        if total < 0:
            left += 1

        elif total > 0:
            right -= 1

        elif total == 0:
            print(*answer)
            sys.exit()

print(*answer)
