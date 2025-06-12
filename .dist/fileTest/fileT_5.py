inFp,outFp=None,None
inStr=""
fname=input("소스 파일명 입력: ")
fname2=input("타깃 파일명 입력: ")
inFp=open(fname,"r")
outFp=open(fname2,"w")

inList=inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("완료")