

n= int(input())
h=list(map(int,input().split()))
maxVal = h[0]
maxValIdx = 0
minVal = h[n-1]
minValIdx = n-1

for i in range(0, n):
    if h[i] > maxVal:
        maxVal = h[i]
        maxValIdx = i
    if h[i] <= minVal:
        minVal = h[i]
        minValIdx = i
swaps = maxValIdx
swaps += (n - 1) - minValIdx
if maxValIdx > minValIdx:
    swaps -= 1


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
    
    

