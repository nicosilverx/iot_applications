class Car():
    def __init__(self, name, speed):
        self.__name = name
        if(speed >= 250):
            self.__speed = 250
        else:
            self.__speed = speed
        self.__gear = 1
    def get_name(self):
        return self.__name
    def set_speed(self, speed):
        if(speed >= 250):
            self.__speed = 250
        else:
            self.__speed = speed
    def get_speed(self):
        return self.__speed
    def gear_up(self):
        if(self.__gear <= 6):
            self.__gear += 1
        else:
            self.__gear = 6
    def gear_down(self):
        if(self.__gear <= 1):
            self.__gear -= 1
        else:
            self.__gear = 1
    def get_gear(self):
        return self.__gear

if __name__=="__main__":
    bmw = Car("BMW M5", 250)
    bmw.gear_up()
    print(bmw.get_gear())