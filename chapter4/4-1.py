def vartest(a):
    a=a+1
    print(a+1)

print(vartest(53))
vartest(543)



# 리턴값이 없는 함수이다!
# 그러므로 vartest(53)를 print하면 None 이라는 결과가 나옴
# print문은 함수의 구성요소중 수행할 문장에 해당할 뿐이다
# 하지만 5번줄에서 vartest 함수의 매개변수 a에 53이라는 인수를 넣게되어
# 함수는 수행되고, 새 변수 a는 2번줄에서 54,
# 3번줄에서는 a+1, 즉 55가 print 명령을 받아
# 이런 결과가 나옴