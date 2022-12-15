def fun(a,b,c,d):
    print("hello",a,b,c,d)

fun('a','b','c','d')


#def fun_args(*rahul,ft): #this will not work
def fun_args(ft,*rahul):
    print(type(rahul))   # this will always return tuple .either provide it tuple,list,anything..
    print(type(ft))
    for i in rahul:
        print(i, end=" ")
    print(ft)


#fun_args("Rahul", "Mittal", "is", "learning","python")

a="Normal argument"  #Normal argument should always be called first
li=[1,2,3,4,5]  #passign list
fun_args(a,li)

c=199
#fun_args(li,c)


def fun_kwargs(**rahul):   # Double start means kwargs
    for i,j in rahul.items():
        print("key is ",i , "value is ", j)


dict1 = {"Rahul" : "Programmer",
                "harry" : "Tutor"}
print(type(dict1))
fun_kwargs(**dict1)

#
# def func2(kwargs):
#     for key,value in kwargs.items():
#         print(key,  value)
#
#
# dict1={'a':1, 'b':2}
# print(type(dict))
# func2(dict1)
#
#
# def func3(**kwargs):
#     for key,value in kwargs.items():
#         print(key,  value)
#
#
# func3(a='1',b=2,c=3)