n= int(input())
x=[]

for i in range(n):
    p=map(int,input().split())3
    
    x.append(p)
a=b=c=0    
for i in x:
    a+=i[0]
    b+=i[1]
    c+=i[2]
if a==b==c==0:
    print("YES")
else:
    print("NO")       
    