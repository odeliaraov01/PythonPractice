absent = [2, 5]
no_book = [7]

for student in range(1, 11): # 변수 student에 1부터 10까지 숫자를 생성하여 차례대로 대입한다. 
    if student in absent: # 결석 학생이면
        continue # 아래 문장 실행하지않고 반복 조건으로 돌아간다. 
    elif student in no_book: # 결석 학생이 아니고 책 없는 학생이라면 
        print("오늘 수업 여기까지 한다. {0}는 교무실로 따라와".format(student))
        break # 반복문을 완전히 종료한다. 
    print("{0}, 책을 읽어봐".format(student)) # 책 있는 학생이라면 실행한다. 

    