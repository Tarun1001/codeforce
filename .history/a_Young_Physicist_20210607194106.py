n= int(input())
x=[]

for i in range(0,n):
    p=map(int,input().split())
    print
    x.append(p)
a=b=c=0  
print(x)  
for item in x:
    a+=item[0]
    b+=item[1]
    c+=item[2]
if a==b==c==0:
    print("YES")
else:
    print("NO")       
    