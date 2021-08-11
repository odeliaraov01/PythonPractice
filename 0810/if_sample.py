# weather = input("오늘 날씨는 어때요?")

# if weather == "비" or weather == "눈": 
#     print("우산을 챙기세여")
# elif weather == "미세먼지":
#     print("마스크 챙기시고요")
# else: #모든 조건에 맞지않을때
#     print("준비물 필요 없어요")

temp = int(input("기온은 어때요?"))
if 30 <= temp: 
    print("너무 더우니까 나가지 마세여")
elif 10 <= temp and temp < 30: 
    print("괜찮은 날씨군요")
elif 0 <= temp < 10: 
    print("외투 챙겨요~")
else: 
    print("너무 추우니까 나가지마세요 ")