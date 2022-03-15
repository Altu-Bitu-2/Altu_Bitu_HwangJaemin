import sys

t = int(input())
for i in range(t):
    n = int(sys.stdin.readline())
    nums1 = set(map(int, sys.stdin.readline().split()))
    m = int(sys.stdin.readline())
    nums2 = list(map(int, sys.stdin.readline().split()))
    for num in nums2:
        if num in nums1:
            print(1)
        else:
            print(0)
