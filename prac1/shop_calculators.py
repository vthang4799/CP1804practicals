def main():
    number_of_items = int(input("How many items you buy: "))
    total_price = 0

    for i in range(number_of_items):
        price_of_items = float(input("Price of item is: "))
        total_price += price_of_items
    if total_price > 100:
        price_after_discount = total_price - total_price * 0.1
        print("Total price for {} items is {:.2f}".format(number_of_items, price_after_discount))
    else:
        print("Total price for {} items is {:.2f}".format(number_of_items, total_price))


if __name__ == '__main__':
    main()
