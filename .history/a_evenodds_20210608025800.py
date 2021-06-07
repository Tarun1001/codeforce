    if(n%2==0):
        half = n/2
    else:
        half = n/2 + 1

    if(k<=half):
        return (2*k)-1
    else:
        return 2*(k-half)