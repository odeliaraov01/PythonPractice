#list 사용 

students =["egoing", "sori", "maru"]
grades = [2,1,4]

print("students[1]", students[1])
print("len(students)", len(students))
print("min(grades)", min(grades))
print("max(grades)", max(grades))
print("sum(grades)", sum(grades))

import statistics #평균값 구하기 statistics 사용
print("mean(grades)", statistics.mean(grades))

import random #랜덤함수 사용하기 

print("random.choice(students)", random.choice(students))

