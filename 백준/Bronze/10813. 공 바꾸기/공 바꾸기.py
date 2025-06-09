N, M = map(int,input().split())

# 바구니 마다 처음에 공 번호가 자기 번호와 같음
baskets = []
for i in range(1, N+1):
    baskets.append(i)

# M번 반복하면서 공 교환 > 파이썬 리스트는 0번 부터 시작 
for _ in range(M):
    i,j = map(int,input().split())
    baskets[i-1], baskets[j-1] = baskets[j-1], baskets[i-1]

print(*baskets)