def write_numbers_to_file(numbers, filename):
    with open(filename, "w") as file:
        for num in numbers:
            file.write(str(num) + "\n")


def print_colored_output(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            if "odd" in filename:
                print("\033[91m" + line.strip() + "\033[0m")
            elif "even" in filename:
                print("\033[94m" + line.strip() + "\033[0m")
            else:
                print("\033[92m" + line.strip() + "\033[0m")


user_input = input(
    "Enter 'odd', 'even', or 'numbers' to display corresponding numbers: ")

if user_input == "odd":
    print_colored_output("odd.txt")
elif user_input == "even":
    print_colored_output("even.txt")
elif user_input == "numbers":
    print_colored_output("numbers.txt")
else:
    print("Invalid input. Please enter 'odd', 'even', or 'numbers'.")
