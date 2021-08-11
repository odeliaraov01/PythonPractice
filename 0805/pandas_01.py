import pandas
crime_records = pandas.read_csv('SacramentocrimeJanuary2006.csv')
#print(crime_records)
print(crime_records.head()) # 맨앞 5줄만 출력한다 pandas.head()
#print(crime_records.describe()) #파일의 데이터를 묘사해준다. count, mean, std, min, max...


