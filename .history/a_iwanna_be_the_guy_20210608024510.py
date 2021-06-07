n = int(input())
x=list(map(int,input().split()))
y=list(map(int,input().split()))
z=x+y
z=set(z)
if len(z)==n :print("I become the guy.")
# def sol(z):       
#     for i in range(1,n+1):
#         if i in z:
#             continue
#         else:
#             print("Oh, my keyboard!")
            
#     print("I become the guy.")       
# sol(z)      
            