N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for i in range(N):
    for j in range(i+1, N): #i부터 시작하면 안됨
        for t in range(j+1, N): #여기도 마찬가지로 j부터 시작하면 안 됨.
            if(nums[i]+nums[j]+nums[t] > M):
                continue
            else:
                answer = max(answer, nums[i]+nums[j]+nums[t]) #둘 비교해서 최댓값 찾는 함수 활용
print(answer)
