n=int(input())
def count(n):
    c=0
    while(n):
        n=n//10
        c=c+1
    return(c)
x=n
s=0
c=count(n)
while(n):
    a=n%10
    s=s+a**c
    n=n//10
if(x==s):
    print("armstrong")
else:
    print("not a armstrong")
