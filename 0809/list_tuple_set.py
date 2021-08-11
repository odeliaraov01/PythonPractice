# # 자료구조의 변경
# menu = {"커피", "우유", "주스"}
# print(menu, type(menu)) # class set : 중괄호로 묶인 집합

# menu = list(menu)
# print(menu, type(menu)) # class list : 대괄호로 묶인 집합

# menu = tuple(menu)
# print(menu, type(menu)) # class tuple : 괄호로 묶인 집합 

# menu = set(menu)
# print(menu, type(menu)) # class set


#quiz 
from random import *

users = range(1, 21) # 1부터 20까지 숫자를 생성/ 그럼 users가 range 타입이 됨
users = list(users)
print(users)
shuffle(users)
print(users)

winners = sample(users, 4) # 무작위로 4명 추첨 중 1명은 치킨, 3명은 커피 줌

print("-- 당첨자 발표 --")
print(" 치킨 당첨자: {0}" .format(winners[0]))
print(" 커피 당첨자: {0}". format(winners[1:]))
print("-- 축하합니다 --")


