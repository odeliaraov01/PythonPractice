sentence = '나는 소년이다'
print(sentence)

sentence2 = "나는 예쁜 소년이다"
print(sentence2)

sentence3= """
나는 소년이고 
파이썬은 쉬워요~~~
"""
print(sentence3)


# 슬라이싱 

jummin = "970921-2020202" # 인덱스 값은 0부터 시작한다. 

print("성별: " + jummin[7])
print("연도: " + jummin[0:2]) # WHO[0:N] : 인덱스 0부터 N-1까지 
print("월: " + jummin[2:4]) # (2,3)
print("일: " + jummin[4:6])
print("생년월일:" + jummin[:6]) #처음부터 N-1까지 


