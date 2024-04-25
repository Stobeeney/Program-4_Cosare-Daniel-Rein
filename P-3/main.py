def write_to_file(filename):
    with open(filename, 'w') as file:
        while True:
            line = input("Enter line: ")
            file.write(line + '\n')
            more_lines = input("Are there more lines? (y/n): ")
            if more_lines.lower() != 'y':
                break


write_to_file('mylife.txt')
