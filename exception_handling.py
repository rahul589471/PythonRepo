print("######################## Try, Catch, Exception ################################")
a = input("Enter number 1")
b = input("Enter number 2")

try:
    print("Sum of these 2 numbers are",  int(a)+int(b))
except Exception as e:
    print(e)
else:
    print("This is else line")
finally:
    print("This is finally line")
print("This is imp line")
