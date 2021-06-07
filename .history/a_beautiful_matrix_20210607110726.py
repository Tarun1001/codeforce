# a=[]
# p=q=0
# for i in range(5):
#     b=[]
#     for j in range(5):
#         x=int(input())
#         b.append(b)
#         if x==1:
#             p=i-2
#             q=j-2
#             print(abs(p)+abs(q))
#             break
#     a.append(b)
lst = []

x = y = 0

for i in range(5):

    matrix = input().split()

    lst.append(matrix)

    for j in range(0, 5):

        if(lst[i][j] == "1"):

            x = i-2

            y = j-2

            print(abs(x) + abs(y))
