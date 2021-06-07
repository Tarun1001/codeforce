s=str(input())
s=s[1:-1]
if s=="":
    print(0)
else:    
    c= s.split(",")      
    print( len(set(c)))
