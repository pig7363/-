class MyError(Exception):
    pass

def saynick(nick):
    if nick=="바보":
        raise MyError()
    print(nick)


try:
    saynick("천사")
    saynick("바보")
except MyError:
    print("허용되지 않는 별명입니다")





# raise는 오류를 발생시키는 명령어이다!!!!!!!!
# 오류를 발생시키려면 오류를 정의해주어야만 하기때문
# 1번째 줄에 MyError클래스는 Exception클래스를 상속받아야한다.