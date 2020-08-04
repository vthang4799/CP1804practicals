def main():
    score = float(input("Enter score: "))
    result = define_result(score)
    print(result)


def define_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()