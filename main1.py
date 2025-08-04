#Write a program to create a class Vehicle and perform the following tasks -
# 1. Create an __init__ method with arguments - max_speed and mileage 
# 2. Create an object of class Vehicle and pass the maximum speed and mileage of the car 
# 3. Print the values of max_speed and mileage by using the object
#Project:
class vehicle:
    def __init__(self,max_speed,mileage ):
        self.max_speed=max_speed
        self.mileage=mileage
dodge=vehicle(12,189)
print("the mileage of the dodge is {} and the maxium speed is {}".format(dodge.mileage,dodge.max_speed))