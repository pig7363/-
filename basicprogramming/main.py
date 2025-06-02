from functions import *
def main():
    students = []

    number_of_students = int(input('Number of students: '))
    for n in range(number_of_students):
        student = read_student()
        students.append(student)

    subjects = collect_subjects(students)
    for subject in subjects:
        update_subject(students, subject)

    last_index = len(students) - 1
    while True:
        name = input(f'Which student do you want to see (0-{last_index}, -1 to quit)? ').strip()
        if name == '-1':
            break

        students[int(name)].print_student()


if __name__ == '__main__':
    main()