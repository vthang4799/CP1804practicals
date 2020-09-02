from prac6.guitar import Guitar


def run_test():
    name = "Gibson L-5 CES"
    year = 1922
    cost = 16035.40

    guitar = (name, year, cost)
    other = ('Another Guitar', 2013, 1512.9)
    print("{} get_age() - Expected {}. Got {}".format(guitar.name, 95,
                                                      guitar.get_age()))
    print("{} get_age() - Expected {}. Got {}".format(other.name, 5,
                                                      other.get_age()))
    print()
    print("{} is_vintage() - Expected {}. Got {}".format(guitar.name,
                                                         True,
                                                         guitar.is_vintage()))
    print("{} is_vintage() - Expected {}. Got {}".format(other.name,
                                                         False,
                                                         other.is_vintage()))


if __name__ == '__main__':
    run_test()