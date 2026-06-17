import math;
n=int(input())
n1=n**2
n2=int (str(n1)[::-1])
n3=int(math.sqrt(n2))
n4=int(str(n3)[::-1])
if(n==n4):
    print("adam")
else:
    print("not an adam") 
