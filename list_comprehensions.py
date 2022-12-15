#[expr for val in collection]


li= [];
for i in range(1,10):
    li.append(i**2);

print(li);

li2 = [i**2 for i in range(1,10) if i%5==0];
print(li2);

li3= [i**2 %5 for i in range(1,10)];
print(li3);