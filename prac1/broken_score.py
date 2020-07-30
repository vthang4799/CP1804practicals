def main():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score, please enter again!")
        score = float(input("Enter score: "))
    if score >= 90:
        print("Exellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
if __name__ == '__main__':
    main()