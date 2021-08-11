# 50명의 승객과 매칭 기회가 있을 때, 총 탑승 승객 수를 구하는 프로그램을 작성하시오. 

from random import *

# 내 답안

customer_sum = 0
customer_time = range(5,51)

for i in range(1,51): # 1에서 50이라는 수
    for customer_no in sample(customer_time,1) :
        if 5<= customer_no <=15: 
            print("[{0}] {1}번째 손님 ( 소요시간 : {2}분)".format(1, i, customer_no))
            customer_sum += 1
    
        else:
            print("[ ] {0}번째 손님 ( 소요시간 : {1}분)".format(i, customer_no))

print(" 총 탑승 승객: {0}분".format(customer_sum))
        

# 수정 답안
# randrange(A,B) : A에서 B-1 값 사이에서 하나의 난수 

cnt = 0 # 매칭된 승객 카운트

for i in range(1,51): # 1~50명의 승객 
    time = randrange(5,51) # 5~50분 사이의 소요시간 하나 난수 받아오기 
    if 5 <= time <= 15: #매칭 성공한 경우 
        ptint("[0] {0}번째 손님 (소요시간 : {1}분".format(i,time))
        cnt += 1 
    else: #매칭 실패한 경우
        ptint("[ ] {0}번째 손님 (소요시간 : {1}분".format(i,time))

