n= int(input())
jer=[]
for _ in range(0, n):
        h, a = map(int, input().split(""))
        jer.append((h, a))
def sol(j) :
    count=0
    for i  in range(0,len(j)):
        for j  in range(0,len(j)):
