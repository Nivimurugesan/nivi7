num=input()
k=1
for i in range(len(num)-1):
    ss=num[i]+num[i+1]
    p=int(ss)
    if p<=26 and num[i]!="0":
        k+=1
if k==3:
    print(k)
else:
    print(k+(k-1)//2)
