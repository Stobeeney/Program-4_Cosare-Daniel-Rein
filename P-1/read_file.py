with open("numbers.txt", "r") as file:
    lines = file.readlines()

even_numbers = []
odd_numbers = []

for line in lines:

    numbers = line.split()

    for num in numbers:
        num = int(num)
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
