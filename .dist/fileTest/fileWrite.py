outFp=None
outStr=""
fname=input("파일명을 입력하세요: ")

outFp=open(fname,"w")

while True:
    outStr=input("내용입력:")
    if outStr!="":
        outFp.writelines(outStr + "\n")
    else:break

outFp.close()
print("정상")