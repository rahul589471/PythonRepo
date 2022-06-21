n= int(input("Enter the number"))
flag= input("Enter Flag - True or False")
print(flag)

# logic
i=1;

if flag==True:
    while i <= n:
        j = 1;
        while j <= i:
            print("*", end='')
            j = j + 1;
        print()
        i = i + 1;
else:
    while i <= n:
        j = n;
        while j >= i:
            print("*", end='')
            j = j-1;
        print()
        i = i + 1;
