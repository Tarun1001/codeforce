s= str(input())
fs=""
for i in s:
    if(i  not in fs):
        fs=fs+ i
    else:
        continue   
if "hello" in fs:
    print("YES")   