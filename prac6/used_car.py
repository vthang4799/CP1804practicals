"""CP1404/CP5632 Practical - Client code to use the Car class."""
# Note that the import has a folder (module) in it.

from prac6.car import Car


def main():
    """Demo test code to show how to use car class."""
    my_car = Car(180)
    my_car.drive(30)
    print("fuel =", my_car.fuel)
    print("odo =", my_car.odometer)
    print(my_car)

    print("Car {}, {}".format(my_car.fuel, my_car.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=my_car))

    # 1. Create new Car object called limo and set the fuel to 100
    limo = Car(100)

    # 2. Add 20 more units of fuel to this new car object using the add method
    limo.add_fuel(20)

    # 3. Print the amount of fuel in the limo car
    print("Limo fuel = ", limo.fuel)

    # 4. Attempt to drive 115
    limo.drive(115)

    # 5. Print the car's odometer reading
    print("Odo = ", limo.odometer)




main()