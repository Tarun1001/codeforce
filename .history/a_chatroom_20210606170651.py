s= str(input())
fs=""
for i in s:
    ifi  not in fs:
        fs=fs+ i
    else:
        continue   
if "hello" in fs:
    print("YES")
else:
    print("NO")       