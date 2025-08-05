class parrot:
    #commint creating class varible
    species="bird"
    #creating class construter
    def __init__(self,name,age):
        self.name=name
        self.age=age
#initialize object of the class
blue=parrot("blue",4)
red=parrot("Red",7)
print("the first parrot is {} and his age is {} and the both belong to the species {}".format(blue.name,blue.age,blue.species))
print("the second parrot is {} and his age is {} and the both belong to the species {}".format(red.name,red.age,red.species))

