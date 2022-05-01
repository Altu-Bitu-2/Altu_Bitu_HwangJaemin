import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
count = 0

for i in range(n):
    newNums = nums[:i] + nums[i+1:]
    left = 0
    right = len(newNums) - 1
    while left<right:
        result = newNums[left] + newNums[right]
        if result == nums[i]:
            count += 1
            break
        elif result < nums[i]:
            left += 1
        else:
            right -= 1
print(count)
