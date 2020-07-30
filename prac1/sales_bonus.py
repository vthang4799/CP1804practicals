def main():
    price_sales = float(input("Enter the sales: $"))
    while True:
        if price_sales < 1000:
            total_sales = price_sales * 0.1
            print("Sales are under $1000, you get 10% bonus is", total_sales)
        else:
            total_sales = price_sales * 0.15
            print("Sales are $1000 and over, you get 15% bonus is", total_sales)
        break
if __name__ == '__main__':
    main()

