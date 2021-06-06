x= str(input)
x=x.lower
s=""
v=["a", "o", "y", "e", "u", "i",]
for i in range(0,len(x)):
    if (x[i] not in v):
        s=s+"."
        s=s+x[i]
print(s)        
    