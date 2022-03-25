r, b = map(int, input().split())
L = 0
W = 0
for i in range(1, r+b+1):
    W = i
    L = (r+b+1)//i
    if ((L*2+(W-2)*2 == r) and ((L-2)*(W-2) == b)):
        print(max(L, W), min(L, W))
        break
    
