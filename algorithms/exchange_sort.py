n=list(map(int,input().split()))
l=len(n)
for i in range(l):
    for j in range(l):
        if(n[i]<n[j]):
            n[i],n[j]=n[j],n[i]
print(n)
