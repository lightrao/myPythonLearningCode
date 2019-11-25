class Robot:
    def __init__(self, n, c, w):
        self.name = n
        self.color = c
        self.weight = w
        
    def introduce_self(self):
        return "My name is " + self.name + '.'


class Person:
    def __init__(self, n, p, i, r=None):
        self.name = n
        self.personality = p
        self.isSitting = i
        self.robot_owned = r

    def sit_down(self):
        self.isSitting = True

    def stand_up(self):
        self.isSitting = False

    def talk(self):
        if self.isSitting == True:
            state = 'sitting'
        else:
            state = 'standing'
        return 'My name is ' + self.name + '.' + ' I am ' + state + '.'

    def describe_pet(self):
        return 'My robot is ' + self.robot_owned.name + '.' + ' Introduce youself: ' + '"' + self.robot_owned.introduce_self() + '"' 


r1 = Robot("Tom", "red", 30)
r2 = Robot("Jerry", "blue", 40)
p1 = Person("Alice", "aggressive", False, r2)
p2 = Person("Becky", "aggressive", True, r1)
print(p1.robot_owned.introduce_self())
print(p2.robot_owned.introduce_self())
p1.sit_down()
print(p1.talk())
print(p1.describe_pet())

