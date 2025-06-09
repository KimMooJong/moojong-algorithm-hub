# 바구니 M
M, N = map(int,input().split())
baskets = [0] * M

# 공 N번 넣는 코드
for _ in range(N):
    i, j, k = map(int,input().split())
# i~j까지 바구니에 공 k를 넣을 거임
# _ 반복할 때 변수 이름이 필요 없을 때 쓰는 거임

    for v in range(i-1,j): # 리스트는 0부터 시작하니 i-1부터 시작
        baskets[v] = k

print(*baskets) # *를 쓰면 리스트를 공백으로 나누어 출력