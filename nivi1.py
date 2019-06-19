num=int(input())
li=list(map(int,input().split()))

rr=[]
for i in range(num):
	if li[i]==i:             
		rr.append(i)
		
if len(rr)==0:
	print(-1)
else:
	for i in rr:
		print(i,end=" ")
