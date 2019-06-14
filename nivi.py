mm=int(input())
nn1=list(map(int,input().split()))
temp=[]
while(len(nn1)!=0):
  if len(nn1)>1:
    temp.append(max(nn1))
    temp.append(min(nn1))
    nn1.remove(max(nn1))
    nn1.remove(min(nn1))
  else:
    temp.append(max(nn1))
    nn1.remove(max(nn1))
print(*temp,end="")  
