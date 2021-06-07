n= int(input())
x=[]

for i in range(0,n):
    p=list(map(int,input().split()))
    x.append(p)
0.
..33
2.a=b=c=0  
for item in x:
    a+=item[0]
    b+=item[1]
    c+=item[2]
if a==b==c==0:
    print("YES")
else:
    print("NO")       
    