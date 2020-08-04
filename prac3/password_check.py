def main():
    password = input_password()
    masked_password = process_password(password)
    print(masked_password)


def input_password():
    password = input("Enter your password: ")
    while not valid_password(password):
        print("Enter a password of at least 8 characters to 20 characters")
        password = input("Enter your password: ")
    return password


def valid_password(password):
    return 8 <= len(password) <= 20


def process_password(password):
    printed_password = ("*" * len(password))
    return printed_password


if __name__ == '__main__':
    main()
