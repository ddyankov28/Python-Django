def print_numbers():
    numbers_file = open("numbers.txt", "r")
    numbers = numbers_file.read()[:-1].split(",")
    for item in numbers:
        print(item)


if __name__ == '__main__':
    try:
        print_numbers()
    except Exception as e:
        print("Error: ", e)
