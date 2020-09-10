from prac8.unreliable_car import UnreliableCar


def main():
    good_car = UnreliableCar("Mickey Car", 100, 70)
    bad_car = UnreliableCar("Catty Car", 100, 2)

    for i in range(1, 20):
        print("Driving {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))


if __name__ == '__main__':
    main()
