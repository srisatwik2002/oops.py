#no need to change it multiple times
'''
class student:
    def __init__(self,subjects,pet):
        self.subjects=subjects
        self.pet=pet
    @property
    def avm(self):
        total=((sum(self.subjects)+(self.pet))/len(self.subjects))
        return total
    @staticmethod
    def greet():
        return ("hello")

print("________________")
s5=student([100,12,25],20)
s5.pet=55
print(s5.avm)
print(s5.greet())
'''


class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        self.total=(self.phy+self.math+self.chem)/3
        return str(self.total)+"%"
stu1=student(98,97,99)
print(stu1.percentage)

stu1.phy=200
print(stu1.percentage)



