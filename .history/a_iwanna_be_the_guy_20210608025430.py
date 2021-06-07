# n = int(input())
# x=list(map(int,input().split()))
# y=list(map(int,input().split()))
# z=x+y
# z=set(z)
# if len(z)==n :print("I become the guy.") 
# else: print("Oh, my keyboard!")
# def sol(z):       
#     for i in range(1,n+1):
#         if i in z:
#             continue
#         else:
#             print("Oh, my keyboard!")
            
#     print("I become the guy.")       
# sol(z)      
a=int(input())
b=input().split(' ')
b=map(int, b)
c=input().split(' ')
c=map(int, c)
d=[]
m=0

#adding the no. of levels to the list d
for i in range(1,b[0]+1):
	d.append(b[i])
for i in range(1,c[0]+1):
	d.append(c[i])


#checking if all levels are in list or not
for i in range(1,a+1):
	if (not(i in d)):
		m=1
		print ("Oh, my keyboard!")
		break

if (m==0):
	print "I become the guy."            