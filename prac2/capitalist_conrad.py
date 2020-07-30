from prac2 import OUTPUT_file
import random
def main():
    start_price = float(input("$"))
    print("{:,.2f}".format(start_price))
    while start_price > 0.01 and start_price< 1000:
        percentage_change = 0
        if random.randint(1, 2) == 1:
            percentage_change = random.uniform(0, 0.1)
        else:
            percentage_change = random.uniform(-0.05, 0)
        start_price *= (1 + percentage_change)
        print("{:,.2f}".format(start_price))

if __name__ == '__main__':
    main()
