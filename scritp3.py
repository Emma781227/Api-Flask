class Car:
  def __init__(self):  
    self.color = input("Enter car color: ")  
    self.model = input("Enter car model: ")  
    self.year = int(input("Enter car year: "))

  def accelerate(self):  
    print(f"The {self.color} {self.model} is accelerating!")

  def brake(self):
    print(f"The {self.color} {self.model} is braking!")


car = Car()

car.accelerate()  
car.brake()



# class voiture:
    
#     def __init__(self,x,y):
#         self.x = x
#         self.y =y
    
#     def avancer(self):
#         self.x  +=1
#     def reculer(self):
#         self.x -=1

# print(voiture)
        