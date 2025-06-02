marks=[90,25,67,45,80]
number=0
for mark in marks:
    number+=1
    if mark>=60:
        print("%d번 학생, 축하합니다!" %number)
    else:
        continue