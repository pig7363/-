import datetime

day1=datetime.date(2021,12,14)
day2=datetime.date(2023,4,5)


abc=day2-day1 # datetime 모듈의 timedelta 클래스의 객체
print(abc.days)
print(type(day2-day1))





# 즉 datetime을 import한다는것은 파이썬 표준라이브러리에서 datetime이라는 이름을 가진 파이썬 파일을 불러온다는 소리이다.
# datetime.date는 datetime이라는 이름을 가진 파일 안에 date라는 클래스의 객체를 생성했다고 할 수 있다.