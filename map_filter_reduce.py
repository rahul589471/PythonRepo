from functools import reduce

print("########################### Lambda ########################################")

def power(a,b):
    return a**b

c= power(3,2)
print(c)

pow =(lambda x,y:x**y)
"""unnamed function"""
print(pow(3,2))

print("########################### Map ########################################")

li = [1,2,3,4,5]
m =map(lambda x:x**3, li)
print(list(m))


print("########################### Filter ########################################")

li= [1,2,3,4,5]
f = filter(lambda x : x%2,li)
print(list(f))


print("########################### Reduce ########################################")

li=[10,20,30,40,50]
'''
x  y   r
10 20  10
10  30  10
10  40  10
10  50  10

'''
r= reduce(lambda x,y:x%y,li)
print(r)