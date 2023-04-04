class TempConversion:
    def __init__(self, temp=1):
        self._temp = temp


class CelsiusToFahrenheit(TempConversion):
    def conversion(self):
        return (self._temp * 9) / 5 + 32


class CelsiusToKelvin(TempConversion):
    def conversion(self):
        return self._temp + 273.15


class FahrenheitToCelcius(TempConversion):
    def conversion(self):
        return (self._temp - 32) * 9 / 5


class KelvinToCelcius(TempConversion):
    def conversion(self):
        return (self._temp - 273.15)


tempInCelsius = float(input("Enter the temperature in Celsius: "))
CelsiusToKelvin = CelsiusToKelvin(tempInCelsius)
print(str(CelsiusToKelvin.conversion()) + " Kelvin")
CelsiusToFahrenheit = CelsiusToFahrenheit(tempInCelsius)
print(str(CelsiusToFahrenheit.conversion()) + " Fahrenheit")
tempInFahrenheit = float(input("Enter the temperature in Fahrenheit: "))
FahrenheitToCelcius = FahrenheitToCelcius(tempInFahrenheit)
print(str(FahrenheitToCelcius.conversion()) + " Celsius")
tempInKelvin = float(input("Enter the temperature in Kelvin: "))
KelvinToCelcius = KelvinToCelcius(tempInKelvin)
print(str(KelvinToCelcius.conversion()) + " Celsius")