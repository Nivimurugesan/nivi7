num=int(input())
li2=list(map(int,input().split()))
for j in range(0,len(li2)):
    if(li2[j]%2==0 and j%2!=0):
            print(li2[j],end=" ")
    elif(li2[j]%2!=0 and j%2==0):
            print(li2[j],end=" ")
