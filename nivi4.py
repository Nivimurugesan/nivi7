num=int(input())
num2=input()
num3=''
for i in num2:
    if i in num3 and i!=" ":
        print(int(i))
        break
    else:
        num3+=i
if num3==num2:
    print("unique")
