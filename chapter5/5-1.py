class Fourcal:
    def __init__(self,first,second):
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
# setdata는 add,sub,mul,div의 사용을 용이하게 하기위헤 변수의 값을 설정하는것이다.
    def add(self):
        result=self.first+self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def div(self):
        result=self.first/self.second
        return result


# class SafeFourcal(Fourcal):
#     def div(self):
#         if self.second==0:
#             return 0
#         else:
#             return self.first/self.second
# a=SafeFourcal(4,0)
# print(a.div())


a=Fourcal(4,5)
print(a.div())