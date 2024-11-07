#avg of three subjects

#method1
class student:
    def __init__(self,tel,hin,eng):
        self.tel=tel
        self.hin=hin
        self.eng=eng
    def avm(self):
         total=((self.tel+self.hin+self.eng)/3)
         return total
s1=student(100,50,25)
print(s1.avm())

#method2
class student:
    def __init__(self,**subjects):
        self.subjects=subjects
    def avm(self):
        total=(sum(self.subjects.values())/len(self.subjects))
        return total

s2=student(tel=100,hin=50,eng=25)
print(s2.avm())

#method3
class student:
    def __init__(self,*subjects):
        self.subjects=subjects
    def avm(self):
        total=(sum(self.subjects)/len(self.subjects))
        return total

s3=student(100,50,25)
print(s3.avm())

#method4
class student:
    def __init__(self,subjects):
        self.subjects=subjects
    def avm(self):
        total=(sum(self.subjects)/len(self.subjects))
        return total

s4=student([100,50,25])
print(s4.avm())

#method5 - using property as a getter

class student:
    def __init__(self,subjects):
        self.subjects=subjects
    @property
    def avm(self):
        total=(sum(self.subjects)/len(self.subjects))
        return total
    @staticmethod
    def greet():
        return ("hello")


s5=student([100,12,25])
print(s5.avm)
print(s5.greet())





