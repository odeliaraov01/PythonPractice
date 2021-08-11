#tuple 
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

name = "김종국"
age = 20
hobby = " 코딩"

print( name, age, hobby)

(name, age, hobby) = ("윤지영", 25, "놀고먹기")
print(name, age, hobby) 

# 집합 set 
# 중복 허용 안됨, 순서 없음

my_set = {1,2,3,3,3}
print(my_set) #중복 허용 안되기 떄문에 1,2,3 만 출력됨 

java ={"유재석", "김태호","양세형"}
python = set(["유재석", "박명수"])

#java와 python을 둘다 할 수 있는 사람은? 
print(java & python) # set 교집합 
print(java.intersection(python))

#합집합 (java 또는 python 둘중 하나라도 할 수 있는 개발자)
print(java | python)
print(java.union(python))
