#complex numbers
class complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def shownumber(self):
        return f"{self.real}i + {self.img}j"
    def __add__(self,num2):
        newreal=self.real + num2.real
        newimg=self.img + num2.img
        return complex(newreal,newimg)
num1=complex(1,3)
print(num1.shownumber())
num2=complex(4,6)
print(num2.shownumber())
print(num1.__add__(num2).shownumber())
num4=num1+num2
print(num4.shownumber())
