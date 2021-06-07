n,k = map(int,input().split(" "))
if(n%2==0):
    half = int(n/2)
else:
    half = int(n/2) + 1
if(k<=half):
    print( (2*k)-1)
else:
    print( int(2*(k-half))+1)