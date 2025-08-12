class minecraft:
    def __init__(self,name,hearts,rating):
        self.hearts=hearts
        self.rating=rating
        self.name=name

crepper=minecraft("crepper",4,0)
print("the {} a mob that give {} hearts of damage rating {} stars from me :)".format(crepper.name,crepper.hearts,crepper.rating))
enderdragon=minecraft("enderdragon",10,4.5)
print("the {} a mob that give {} hearts of damage rating {} stars from me :)".format(enderdragon.name,enderdragon.hearts,enderdragon.rating))