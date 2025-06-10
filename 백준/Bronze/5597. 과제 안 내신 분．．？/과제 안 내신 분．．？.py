# 전체 학생수 30명
students = list(range(1,31))

# 28명의 제출자 번호를 입력 받아 리스트 제거
for i in range(28):
    submit = int(input())
    students.remove(submit)

# 미제출자 오름차순 정렬
print(students[0])
print(students[1])
