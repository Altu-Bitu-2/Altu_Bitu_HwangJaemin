import sys

s = sys.stdin.readline().rstrip()

words = set()

for i in range(1, len(s)+1):
    for j in range(len(s)-i+1):
        word = s[j:j+i]
        words.add(word)
        
print(len(words))
