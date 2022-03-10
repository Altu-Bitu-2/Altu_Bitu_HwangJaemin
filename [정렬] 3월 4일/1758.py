import sys

num = int(sys.stdin.readline().strip())
tipList = []
totalTip = 0
for i in range(num):
    tipList.append(int(sys.stdin.readline().strip()))
    
tipList.sort(reverse = True)

for i in range(len(tipList)):
    tip = tipList[i] - i
    if tip>0:
        totalTip += tip
        
print(totalTip)
