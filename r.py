
class MyClass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
        self.c = a + b

    def sum(self):
        print("Ans:",self.c)
    
    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        if self.b != 0:
            return self.a / self.b

a=int(input("Enter the a:"))
b=int(input("Enter the b:"))
c = input("enter the event")
obj = MyClass(a,b)

if c == "add":
    obj.sum()
if c == "sub":
    obj.sub()
