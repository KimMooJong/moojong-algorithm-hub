numbers = []
for i in range(9):
    num = int(input())
    numbers.append(num)

#최댓값 구하기
max_num = max(numbers)

#최댓값의 위치구하기
position = numbers.index(max_num) + 1

print(max_num)
print(position)