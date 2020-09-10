from prac8.taxi import Taxi


def main():
    taxi = Taxi("Prius 1", 100)
    taxi.drive(40)
    print("Current fare: {}".format(taxi.get_fare()))

    taxi.start_fare()
    taxi.drive(100)
    print("Current fare: {}".format(taxi.get_fare()))


if __name__ == '__main__':
    main()