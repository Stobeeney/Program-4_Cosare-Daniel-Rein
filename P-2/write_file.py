def read_student_data(file_path):
    students = []
    with open(file_path, 'r') as file:
        for line in file:
            name, gwa = line.strip().split(',')
            students.append((name, float(gwa)))
    return students


def find_lowest_gwa(students):
    lowest_gwa = float('inf')
    lowest_gwa_student = None
    for student in students:
        name, gwa = student
        if gwa < lowest_gwa:
            lowest_gwa = gwa
            lowest_gwa_student = student
    return lowest_gwa_student


def main():
    file_path = 'students_gwa.txt'
    students = read_student_data(file_path)
    lowest_gwa_student = find_lowest_gwa(students)
    if lowest_gwa_student:
        name, gwa = lowest_gwa_student
        print(f"The student with the highest GWA is \033[91m{
              name}\033[0m with a GWA of \033[94m{gwa}\033[0m.")
    else:
        print("No student data found.")


if __name__ == "__main__":
    main()
