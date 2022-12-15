def rec(x):
        if x==1:
            return 1
        output = x * rec(x-1)
        return output


n =int(input("Enter a number"))


print(rec(n))
