inFp = None
inStr=""
inFp = open("C:\\Users\\LG\\Desktop\\python실습\\.dist\\fileTest\\data.txt","r",encoding='UTF8')
n=1


while True:
    inStr=inFp.readline()
    if inStr =="":
        break;
    print(n,":",inStr,end="")
    n+=1



inFp.close()
