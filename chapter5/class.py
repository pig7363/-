import random

def randompop(data):
    number=random.randint(0,len(data)-1)
    return data.pop(number)
# pop(x) --> 리스트의 "x번쨰" 요소를 리턴해줌


if __name__=="__main__":
    data=[1,2,3,4,5]
    while data:
        print(randompop(data))