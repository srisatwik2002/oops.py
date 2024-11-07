# class circle:
#     def __init__(self,r):
#         self.r=r
#     def area(self):
#         return 3.14* (self.r**2)
#     def perimeter(self):
#         return 2*3.14*self.r
# c1=circle(21)
# print(c1.area())
# print(c1.perimeter())



# class employee:
#     def __init__(self,role,dept,sal):
#         self.role=role
#         self.dept=dept
#         self.sal=sal
#     def showdetails(self):
#         return f"role : {self.role}, salary: {self.sal}, dept: {self.dept}"
# class engineer(employee):
#     def __init__(self,name,age,role,dept,sal):
#         self.name=name
#         self.age=age
#         super().__init__(role,dept,sal)
#     def showengineer(self):
#         return f"{self.role},{self.dept},{self.sal},{self.name},{self.age}"
# e2=engineer("qwerty",23,"hr","it",25000)
# print(e2.role,e2.age,e2.name,e2.sal,e2.dept)
#
#
# e1=employee("intern","it",5000)
# print(e1.role,e1.dept,e1.sal)






class Animal:
    def sound(self):
        return "animal sounds"
class dog(Animal):
    def sound(self):
        return "dogbarks"
class cat(Animal):
    def sound(self):
        return "meows"

a1=dog()
print(a1.sound())

class measurements:
    def area(self,r):
        self.r=r
        return self.r**2
    def area(self,l,b):
        self.l=l
        self.b=b
        return self.l * self.b
ar1=measurements()
print(ar1.area(5))

