n= int(input())
h=list(map(int,int(input().split())))
count=0
c2=0
x=max(h)
y=min(h)

for i in range(n):
    if (h[i]==x):
        count= count+i
    
    
    
