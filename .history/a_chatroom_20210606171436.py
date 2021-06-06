
def chatroom():
    s= str(input())
    m="hello"
    x=0 
    for i in range(len(s)):
        if s[i] ==m[x]:
            x=x+1
        if x==5:
            print("YES")
    return "NO"   
chatroom()         




