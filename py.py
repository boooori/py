class Car :
    def __init__(self, model, color):
        self.model = model
        self.color = color

    def info(self):
        print("Model:",self.model, ",Color :", self.color)

class CarDrive(Car):

    def info(self) :
        print("The model of this car is %s." %self.model)
        print("The color is %s." % self.color)
bmw = CarDrive("BMW","white")
bmw.info()
