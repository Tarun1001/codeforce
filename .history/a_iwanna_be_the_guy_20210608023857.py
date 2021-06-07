n = int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=x+y
for i in range(1,n+1):
    if i in x:
        continue
    else:
        print("")