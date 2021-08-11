
# # print(random()) # 0.0 ~1.0 미만의 임의의 값 생성 
# # print(random() *10 ) # 0.0 ~ 10.0 미만의 임의의 값 생성 
# # print(int(random() *10)) # 0 ~ 10 미만의 임의의 값 생성 
# # ptint(int(random() *10) + 1) # 1~ 10 미만의 임의의 값 생성 

# print(int(random()* 45) + 1) # 1 ~ 45 미만의 임의의 값 생성 


# QUIZ 
from random import *
date = randint(4, 28) # radint(a, b) : a 이상 b 이하까지 랜덤으로 int 값 생성함 
print("오프라인 스터디 모임 날짜는 매월 " + str(date) +"일로 선정되었습니다") # print()는 문자열 출력 함수이기 때문에 str(변수)로 감싸줘야 한다. 




