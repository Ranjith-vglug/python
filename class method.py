# class student:
#     name='ranjith'
#     age='34'
#     def raja():
#         print("Student name:",student.name)
#         print("Student age:",student.age)

# student.raja()
# print(student.__dict__)
# print(getattr(student,"raja"))
# getattr(student,"raja")()
# student.__dict__['raja']()

class student:
    name='ranjith'
    age=34
    def raja(self,Gender,age):
        print("Student name:",student.name)
        print("Student age:",age)
        print("Student Gender:",Gender)
a = student()
# a.raja()
# student.raja(o)
student.raja(a,"male","21")
