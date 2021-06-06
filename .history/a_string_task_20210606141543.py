x= str(input)
a=""
v=["a", "o", "y", "e", "u", "i",]
for i in range(0,len(x)):
    if (x[i].lower in v):
        x[i]=""
    elif (i.isupper):
        x[i]=x.lower
        else:
            x
