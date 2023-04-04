class DistanceConversion:
    def __init__ (self, distance):
        self.__distance = distance

    def distance1(self):
        return self.__distance * 100

    def distance2(self):
        return self.__distance / 1000

    def distance3(self):
        return self.__distance * 39.37

    def display(self):
        print("Meter to Centimeter: ", self.distance1(), "cm")
        print("Meter to Kilometer: ", self.distance2(), "km")
        print("Meter to Inches: ", self.distance3(), "in")

distance = DistanceConversion(float(input("Distance: ")))
distance.display()
distance.__distance = 5
distance.display()