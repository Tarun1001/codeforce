n= int(input())
h=list(map(int,int(input().split())))
c1=0
c2=0
x=max(h)
y=min(h)

for i in range(n):
    if (h[i]==x):
        c1= c1+i
    if(h[i]==y):
        c2=c2+i
print(c1+c2)    
    
    
