FILENAME = "subject_data"


def main():
    data = formatting_subject_details()
    print(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print(parts[0], "is taught by", parts[1], "and has", parts[2], "students")
        print("----------")
    input_file.close()

def formatting_subject_details():
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()
        parts = line.split(',')
        print("{} is taught by {} and has {} students".format(parts[0], parts[1], parts[2]))



main()