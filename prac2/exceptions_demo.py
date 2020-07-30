def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
        #this occur when what you enter is not a number or enter a floating point number
    except ZeroDivisionError:
        fraction = 0
        print(fraction)
        #this occur when you enter the value of denominator = 0
    print("Finished.")
if __name__ == '__main__':
    main()