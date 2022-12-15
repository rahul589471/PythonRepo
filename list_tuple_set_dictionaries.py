print( "############################################# List ################################################## ")
# List is mutable i.e. It can be changed
li = ['a', 2, 3, 'A', 'Rahul', 'wer']

# for i in li:
#     print(i)

for index, element in enumerate(li):
    print('index is', index, 'element is', element)

print(li.append('Mittal'))
print(li.count('a'))
l2 = []
print(l2.copy())
print(l2)

print(li.insert(18, 'd'))
print(li.index('d'))
print(li.reverse())
print(li)
li[5] = 'fff'
print(li)
print(len(li))
print(li.clear())
print(li)


print("############################################# Tuple ##################################################")
# Tuple is Immutable i.e. It can not be changed


tup1 =(1,2,3,4,5,'a','vb','ghjkl')
print(tup1)

#tup[2] ='Rahul'   --> This is not allowed

print(tup1.count('a'))


print("############################################# Dictionary ################################################## ")
dict1 = {1: 'Rahul',
         2:'Mittal',
         3:'Abc',
         4:'DFR'}

print(dict1)
print(dict1.keys())
print(dict1.values())

for key,value in dict1.items():
    print('key is' , key , 'value is' , value)

dict1.update({5:'fffffff'})
print(dict1)


