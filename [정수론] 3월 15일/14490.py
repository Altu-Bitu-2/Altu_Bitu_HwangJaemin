from sys import stdin
from math import gcd

n, m = map(int, stdin.readline().split(':'))

num = gcd(n, m)

print(f"{n//num} : {m//num}")
