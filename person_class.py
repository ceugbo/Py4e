class Person:
    def __init__(self,name:str, age:int):
        self.name = name
        self.age = age
    
    def talk(self):
        print(f"My name is {self.name} and I am {self.age} years old.")

p1 = input("Enter your name then your age separated by a comma: ")
p1 = p1.split(',')
#print (p1)
p2 =Person(p1[0], p1[1])
p2.talk()