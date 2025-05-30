a, b, c = map(int,input().split())

if a == b == c:
    # 3개가 모두 같을 때
    print(10000 + a * 1000)
elif a == b or a == c:
    # 2개가 같을때
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a,b,c)*100)