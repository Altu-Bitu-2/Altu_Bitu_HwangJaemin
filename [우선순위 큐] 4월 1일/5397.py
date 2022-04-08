import sys
input = sys.stdin.readline

t = int(input())

for i in range(t):
    stackL = []
    stackR = []
    password = input().replace('\n', '')
    for word in password:
        if word == '-':
            if stackL:
                stackL.pop()
        elif word == '<':
            if stackL:
                stackR.append(stackL.pop())
        elif word == '>':
            if stackR:
                stackL.append(stackR.pop())
        else:
            stackL.append(word)

    stackL.extend(reversed(stackR))
    print(''.join(stackL))
