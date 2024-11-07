class student:
    nationality="indian"
    def __init__(self,fname,lname,age):
        self.fname=fname
        self.lname=lname
        self.age=age
    # @property
    # def hello(self):
    #     print(f"hello {self.fname}{self.lname} how are you")
    def hello(self):
        return f"hello {self.fname}{self.lname} how are you"

s1=student("qwerty","asdfgh",10)
print(s1.fname)

stu=student("asdfgh","zxcvbn",20)
stu.nationality="american"

print(stu.fname)
print(stu.nationality)
print(stu.hello())

print(student.nationality)