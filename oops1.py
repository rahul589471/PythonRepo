class Phone:
    Brand = 'Samsung'

    def __init__(self, a, b):
        self.color = a

    def print_phone(self):
        return self.color

    @classmethod
    def change_brand(cls,b):
        cls.Brand = b
        return cls.Brand


p1 = Phone('Red', 2)

'''x = p1.print_phone()
print(x)

print(p1.Brand)
p1.Brand = 'Apple'
print(p1.Brand)

print(p1.__dict__)
print(Phone.Brand) '''

#p1.Brand = 'Apple'
p1.change_brand('XYZ')
print(p1.Brand)
