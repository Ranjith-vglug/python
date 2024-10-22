# PROPERTY DECORATOR GETTER SETTER
class student:
    def __init__(self,total):
        self._total=total
    def avg(self):
        return self._total/5
    @ property  # To get the value from private variable 
    def total(self):
        return self._total
    
    @ total.setter # To set the value for the private variable
    def total(self,t):
        if t<0 or t>500:
            print("Invalid total because of highest score")
        else:
            self._total=t
o1=student(590)
print("Average of ",o1.total,"is",o1.avg())
print("Total:",o1.total)
print("Average:",o1.avg())
o1.total=900
print("Total:",o1.total)
