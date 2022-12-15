

n= int(input("Enter the number"))
flag= int(input("Enter Flag - 0 or 1"))


'''
*
* *
* * *
* * * *
'''

if flag==1:
    flag_bool = True
else:
    flag_bool = False

if flag_bool:
    for i in range(n + 1):
        for j in range(i):
            print("*", end=" ")
        print()
else:
    for i in range(n,0,-1):
        for j in range(i):
            print("*", end=" ")
        print()
























# logic
i=1;

# if flag==True:
#     while i <= n:
#         j = 1;
#         while j <= i:
#             print("*", end='')
#             j = j + 1;
#         print()
#         i = i + 1;
# else:
#     while i <= n:
#         j = n;
#         while j >= i:
#             print("*", end='')
#             j = j-1;
#         print()
#         i = i + 1;
