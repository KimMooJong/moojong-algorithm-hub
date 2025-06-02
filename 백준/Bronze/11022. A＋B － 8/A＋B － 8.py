import sys
T = int(sys.stdin.readline())
c = 0

for i in range(T):
    a,b = map(int,sys.stdin.readline().split())
    c = a+b
    i += 1
    print(f'Case #{i}: {a} + {b} = {c}')