class car:
    top = "rooftop"
    @classmethod
    def changetop(cls, top):
        cls.top = top
        return (top)
    @staticmethod
    def start():
        print("start")
    @staticmethod
    def stop():
        print("stop")
    def __init__(self,wheels):
        self.wheels=wheels
class ambassador():
    def __init__(self,colour):
        self.colour=colour
class toyota(car):
    def __init__(self,milage,wheels): #single
        self.milage=milage
        super().__init__(wheels)
class nano(toyota): #multilevel
    def __init__(self,price,milage,wheels):
        self.price=price
        super().__init__(milage,wheels)
class fortuner(ambassador):
    def __init__(self,etype,colour):
        self.etype=etype
        super().__init__(colour)
class elexsi(toyota,fortuner):#muliple
    def __init__(self,engine,milage,wheels,etype,colour):
        self.engine=engine
        toyota.__init__(self,wheels,milage)
        fortuner.__init__(self,etype,colour)
c5=elexsi("v4",32,4,"petrol","black")
print(c5.etype,c5.colour,c5.engine,c5.milage,c5.wheels)
print("______________________________________________________")
c6=nano(250000,28,4)
print(c6.milage,c6.wheels,c6.price)
c1=car(4)
c2=ambassador("white")
c3=toyota(24,4)
c4=fortuner("electric","red")
print("______________________________________________________")

print(c1.wheels,c2.colour,c3.wheels,c3.milage,c4.etype,c4.colour)

ca1=car(4)
print(ca1.changetop("roofless"))