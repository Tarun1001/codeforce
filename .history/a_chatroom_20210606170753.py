s= str(input())
fs=""
for i in s:
    if i  not in fs:
        fs=fs+ i
      
if "hello" in fs:
    print("YES")
else:
    print("NO")       