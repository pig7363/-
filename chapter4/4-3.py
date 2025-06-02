f= open("C:/doit/새파일.txt",'w')
for i in range(1,11):
    
    f.write("%d번째 줄입니다.\n" %i)

f.close()