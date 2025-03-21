print("입력 진수 결정(16/10/8/2):")
a=int(input())
print("값입력:")
if a==16:
    b=input()
    b=int(b,16)
if a==10:
    b=int(input())
if a==8:
    b=input()
    b=int(b,8)
if a==2:
    b=input()
    b=int(b,2)
print('16진수>>',hex(b))
print("10진수>>",b)
print("8진수>>",oct(b))
print ("2진수>>",bin(b))




