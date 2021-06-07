n= int(input())
jer=[]
for _ in range(0, n):
    h, a = map(int, input().split(" "))
    jer.append((h, a))
def sol(jer) :
    count=0
    for i  in range(0,len(jer)):
        for j  in range(0,len(jer)):
            if i==j:
                continue
            hometeamHomejersey= jer[i][0]
            awayteamAwayjersey= jer[i][1]
            if hometeamHomejersey==awayteamAwayjersey:
                count+=1
    return count
sol(jer)                
