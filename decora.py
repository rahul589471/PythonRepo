def decor(func):
    print("Executing")
    def inner(x,y):
        if y>x:
            y,x=x,y
        return func(x,y)
    return inner

@decor
def div(a,b):
    return a/b;


ans= div(2,3)
print(ans)