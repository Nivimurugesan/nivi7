ee=int(input())
xx=list(map(int,input().split()))
li=max(x)
ee,ff=0,0
for a in range(0,len(xx)):
  for b in range(a+1,len(xx)):
    if abs(xx[a]+xx[b])<l:
      ee,ff=xx[aa],xx[bb]
      li=abs(ee+f)
print(ee,ff)
