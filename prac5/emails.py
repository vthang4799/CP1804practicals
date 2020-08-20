def main():
    name_from_email = {}
    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input("Is your name {}? (Y/n) ".format(name))
        if confirmation.upper() != "Y" and confirmation != "":
            name = input("Name: ")
        name_from_email[email] = name
        email = input("Email: ")

    for email, name in name_from_email.items():
        print("{} ({})".format(name, email))


def get_name_from_email(email):
    name_recognition = email.split('@')[0]
    parts = name_recognition.split('.')
    name = " ".join(parts).title()
    return name


main()