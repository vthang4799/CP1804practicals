import random


def main():
    temperature = random.randint(-100,100)
    celcius = convert_fahrenheit_to_celcius(temperature)
    fahrenheit = convert_to_fahrenheit(temperature)
    print(fahrenheit, celcius, end='')


def convert_to_fahrenheit(celcius):
    fahrenheit = 9/5 * celcius + 32
    return fahrenheit


def convert_fahrenheit_to_celcius(fahrenheit):
    celcius = 5/9 * (fahrenheit - 32)
    return celcius

if __name__ == '__main__':
    main()

