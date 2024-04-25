def process_integers(input_file):
    with open(input_file, 'r') as f:
        numbers = [int(line.strip()) for line in f.readlines()]

    print("\033[92mIntegers: \033[0m", end="")
    print("\033[92m[", end="")
    print(*numbers, sep=", ", end="")
    print("\033[92m]\033[0m")

    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    print("\033[94mEven numbers: \033[0m", end="")
    print("\033[94m[", end="")
    print(*even_numbers, sep=", ", end="")
    print("\033[94m]\033[0m")

    print("\033[93mOdd numbers: \033[0m", end="")
    print("\033[93m[", end="")
    print(*odd_numbers, sep=", ", end="")
    print("\033[93m]\033[0m")

    even_squares = [num ** 2 for num in even_numbers]
    odd_cubes = [num ** 3 for num in odd_numbers]

    print("\033[94mSquares of even numbers: \033[0m", end="")
    print("\033[94m[", end="")
    print(*even_squares, sep=", ", end="")
    print("\033[94m]\033[0m")

    print("\033[93mCubes of odd numbers: \033[0m", end="")
    print("\033[93m[", end="")
    print(*odd_cubes, sep=", ", end="")
    print("\033[93m]\033[0m")

    with open('double.txt', 'w') as f:
        f.write('\n'.join(map(str, even_squares)))

    with open('triple.txt', 'w') as f:
        f.write('\n'.join(map(str, odd_cubes)))


process_integers('integers.txt')
