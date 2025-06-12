inFp=None
inList=[]
inStr=""
n=1
inFp=open("C:\\Users\\LG\\Desktop\\python실습\\.dist\\fileTest\\data.txt","r",encoding='UTF8')

inList=inFp.readlines()
for inStr in inList:
    print(n,":",inStr,end="")
    n+=1
inFp.close