hour, minute = map(int,input().split())
add_time = int(input())

# 전체 분 단위로 계산
total_minutes = hour * 60 + minute + add_time

# 다시 시와 분으로 나누기
hour = (total_minutes // 60) % 24
minute = total_minutes % 60

print(hour,minute)