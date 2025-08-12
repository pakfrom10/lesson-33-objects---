class Calcarea:
    def __init__(self,L,W):
        self.L=L
        self.W=W
        print("Constructor initialised ")
    def calculate(self):
        print("Area = ",self.L*self.W)

R1=Calcarea(2023,2030)    

R1.calculate()
                                