#사전 
# 변수 = {key: values, key : values ...}

cabinet = {3: "유재석", 100: "김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))

#print(cabinet.get[5]) 오류라서 이후 코드도 실행안된다. 
print(cabinet.get(5, "사용 가능")) # 해당 키에 값이 없더라도 none이 출력된다. (key, "str") : key값이 없으면 str을 출력한다. 
print(3 in cabinet) # key가 cabinet에 있으면 true / 없으면 false 출력된다. 

#string
cabinet = {"A-3" : "유재석", "B-100": "김태호"}
print(cabinet["A-3"])
print(cabinet.get("B-100"))
#print(cabinet.get["A-0"])
print(cabinet.get("A-0", "사용 가능"))

# 새 손님 
print(cabinet)
cabinet["C-20"] = "조세호" # 새로운 데이터 생성
cabinet["A-3"] = "김종국" # 데이터 업데이트
print(cabinet)
del cabinet["A-3"] # 데이터 삭제 
print(cabinet)

#key만 출력
print(cabinet.keys())
#value만 출력
print(cabinet.values())
#key, value 쌍으로 출력
print(cabinet.values())

#claer()
print("사전 비우기")
cabinet.clear()
print(cabinet)