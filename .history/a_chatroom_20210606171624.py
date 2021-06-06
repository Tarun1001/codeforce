m="hello"
def chatroom():
    s= str(input())
    x=0 
    for i in range(len(s)):
        if s[i] ==m[x]:
            x=x+1
        if x==5:
            return "YES"
    return "NO"   
print(chatroom())         




