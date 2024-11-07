#public,private,protected:-
# private
class account:
    def __init__(self,accno,password):
        self.accno=accno
        self.__password=password
    def shpass(self):
        return f"the password is:  {self.__password}"
ac1=account(12345,"abcde")
print(ac1.accno)
print(ac1.shpass())  #1.)it can be used as the method way
print(ac1._account__password)  # 2.)it can be used as the _class__protectedattribute name
#
# there are two ways a private attribute can be accessed
# 1.)which by accessing the method
# which is inside the class associated to revealing the private attribute
# 2.)the _class__protectedattribute name method can be used for revealing the
# protected attribute information


'''
#private method
class account:
    def __init__(self,accno,password):
        self.accno=accno
        self.__password=password
    def shpass(self):
        return f"the password is:  {self.__password}"
    def __hello(self):
        return (f"hello user {self.accno} and your password is {self.__password}")
    def welcome(self):
        return self.__hello()
ac1=account(12345,"abcde")
print(ac1.accno)
print(ac1.shpass())
print(ac1._account__password)
print(ac1.welcome())
# print(ac1.__hello())
# print(ac1.__password)


#protected is using only single underscore _accno,_password etc
#public is used by everybody
'''



