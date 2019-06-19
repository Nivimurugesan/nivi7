pp=int(input())
li=list(map(int,input().split()))
for a in range(0,pp-2):
    for b in range(a+1,pp-1):
        for c in range(b+1,pp):
            if(li[a]+li[b]==li[c]):
                print(li[a], li[b], li[c])
