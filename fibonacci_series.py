# Fibonnaci series
# 0 1 1 2 3 5 8 13 21.....

n= int(input("Enter the number"))

def fibonacci(n):
    a = 0;
    b = 1;
    c = 0;
    if(n==1):
        print(0)
    elif(n==2):
        print(1)
    else:
        print(0, end = " ")
        print(1, end = " ")
        for i in range(n-2):
            c = a + b;
            print(c, end =" ")
            a = b
            b = c


print("Fibonacci without recursion ")
fibonacci(n)


def fibonacci_recursion(n):
    if(n==1):
        return 0
    elif(n == 2):
        return 1
    else:
        return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)

print()
print("Fibonacci with recursion ")
print(fibonacci_recursion(n))



