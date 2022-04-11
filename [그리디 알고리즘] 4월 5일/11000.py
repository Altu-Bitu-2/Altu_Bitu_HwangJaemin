import heapq
import sys
input = sys.stdin.readline


n = int(input())

times = [list(map(int, input().split())) for _ in range(n)]
times.sort()

result = []
heapq.heappush(result, times[0][1])

for i in range(1, n):
    if result[0] > times[i][0]:
        heapq.heappush(result, times[i][1])
    else:
        heapq.heappop(result)
        heapq.heappush(result, times[i][1])

print(len(result))
