f=open("C:/doit/새파일.txt",'r')
while True:
    line=f.readline()
    line=line.rstrip("\n")
    if not line:
        break
    print(line)
f.close()