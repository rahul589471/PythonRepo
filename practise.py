from functools import reduce

'''
comment ....


print(""" Hello
Brother""");

print("hello \n Rahul \t How are you doing ?")

#Format String
name = input("Enter name ");
surname = input("Enter surname");

a = f" name is {name} , surname is {surname}";
print(a);
b = "name is {0} and surname is {1}".format(name,surname);
print(b);

#list
print(li.count(3)) #count of particular element

#tuple

#set

#dictionary


## enumerate

lst =[1,2,3,4,5]

for i in lst:
    print(i);

for index,elem in enumerate(lst):
    print ("index of element :" +str(elem) + " is " + str(index));

    #lambda
'''

# map ,filter & reduce

# filter
li = [3, 6, 7, 8, 98, 76, 4, 3, 7, 9, 45, 6, 77, 88, 55];

odds = list(filter(lambda x: x % 2 == 1, li))
print(odds)

# map
doubles = list(map(lambda x: x * 2, odds));
print(doubles);

# reduce
sum_all = reduce(lambda a, b: a + b, doubles)
print(sum_all)

print(sum((2, 32)))


def xyz():
    """ This is test function"""
    pass


print(xyz())
print(xyz.__doc__)



