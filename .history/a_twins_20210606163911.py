n= int(input())
coins= list(map(int,input().split()))
total= 0
result= 0
coins= sorted(coins,reverse=True)
for i in range(0,len(coins)):
    total = total+ coins[i]


