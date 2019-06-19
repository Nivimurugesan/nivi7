pp,qq=map(int,input().split())
rr={int(rr) for rr in input().split()}
ss={int(ss) for ss in input().split()} 
if(ss.issubset(rr)):
    print("YES")
else:
    print("NO")
