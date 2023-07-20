class TV:
    def __init__(self,power,channel,volume):
        self.power = power
        self.channel = channel
        self.volume = volume
    def info(self):
        print("Power :", self.power)
        print("Channel :", self.channel)
        print("Volume :", self.volume)
    def Turn_on(self):
        print("Turn on")
    def Turn_off(self):
        print("Turn off")
    def set_channel(self,v):
        self.channel = v
    def set_volume(self,v):
        self.volume = v
lugo = TV("True","0","0")
lugo.set_channel("1")
lugo.set_volume("16")
lugo.info()
lugo.Turn_on()
lugo.Turn_off()
        
