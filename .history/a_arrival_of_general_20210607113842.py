

n= int(input())
h=list(map(int,input().split()))
    maxVal = heights[0]
    maxValIdx = 0
    minVal = heights[n-1]
    minValIdx = n-1

    for i in xrange(0, n):
        if heights[i] > maxVal:
            maxVal = heights[i]
            maxValIdx = i

        if heights[i] <= minVal:
            minVal = heights[i]
            minValIdx = i

    swaps = maxValIdx
    swaps += (n - 1) - minValIdx

    if maxValIdx > minValIdx:
        swaps -= 1

    return swaps

# c1=0
# c2=0
# x=max(h)
# y=min(h)

# for i in range(n):
#     if (h[i]==x):
#         c1= i
#     if(h[i]==y):
#         c2=n-1-i
# print(c1+c2)    
    
    

