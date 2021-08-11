#while

# customer = "토르"
# index = 5

# while index >= 1: 
#     print("{0}, 커피가 준비되었습니다. {1}번 남았어요!".format(customer, index))
#     index -= 1
#     if index == 0: 
#         print("커피는 더이상 주문 불가합니다.")

#무한루프 걸리면 ctrl + C로 강제종료 가능하다. 

# customer = "윤지영"
# index = 1

# while True:
#     print("{0}님, 커피가 준비되었어요. {1}번째 호출입니다.". format(customer, index))
#     index += 1
 
customer = "윤지영"
person = "Unknown"

while person != customer : #while은 조건을 만족할 때까지 계속 반복된다. 
    print("{0}님, 커피가 준비되었습니다~". format(customer))
    person = input("이름이 어떻게 되세요?")

 
    