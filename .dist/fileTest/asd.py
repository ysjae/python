inFp,outFp=None,None
inStr,outStr="",""
i=0
secu=0


secuYN=input("1.암호화 2.암호해석중 선택:")
inFname=input("입력 파일명을 입력하세요:")
outFname=input("출력 파일명을 입력하세요:")

if secuYN=="1":
    secu=100
elif secuYN=="2":
    secu=-100

inFp=open(inFname,'r',encoding='UTF-8')
outFp=open (outFname,'w',encoding='UTF-8')

while True:
    inStr=inFp.readline()
    if not inStr:
        break

    outStr=""
    for i in range(0,len(inStr)):
        ch = inStr[i]
        chNum=ord(ch)
        chNum=chNum+secu
        ch2=chr(chNum)
        ourStr=outStr+ch2
    
    outFp.write(outStr)

outFp.close()
inFp.close()
print('%s>%s변환 완료'%(inFname,outFname))
