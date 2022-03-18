import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
print(round(sum(nums)/N))
nums.sort()
print(nums[N//2])
nums_s = Counter(nums).most_common()
#most_common() 함수로 리스트 안의 원소들이 몇 번 등장했는지 알 수 있음.

if len(nums_s) > 1: #입력된 숫자가 여러개일 때
    if nums_s[0][1] == nums_s[1][1]: #두 번째로 큰 수라고 했으니까 둘만 비교하면 됨.
        print(nums_s[1][0])
    else:
        print(nums_s[0][0])
else:
    print(nums_s[0][0])
print(nums[-1]-nums[0])
