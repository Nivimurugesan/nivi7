num=int(input())
aa=list(map(int,input().split()))
cc=[]
co=0
for i in aa:
     if i not in cc:
          cc.append(i)
for j in cc:
     for k in aa:
          if(j==k):
               co=co+1
     if(co==1):
          print(j)
     co=0
