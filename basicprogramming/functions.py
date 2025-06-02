from main import*
# Condition 15
def read_student():
    name = input('Type a student\'s name: ').strip().title()  # Condition 16
    student_id = input(f'Type student ID of {name}: ').strip()

    # Condition 17
    student = Student(name=name, student_id=student_id)
    # Condition 18
    while True:
        line = input('Subject, raw score (Type END to finish)? ').strip()
        # Condition 19
        if line.upper() == 'END':
            break

        # Condition 20
        split = line.split(',')
        if len(split) != 2:
            print('Invalid input. Please type a subject and its score.')
            continue

        # Condition 21
        subject, score = split
        score = Grading(score)
        student.add_subject(subject, score)

    return student

# Condition 22
def collect_subjects(students):
    subjects = []

    for student in students:
        for subject in student.get_subject_names():
            if not subject in subjects:
                subjects.append(subject)

    return subjects

def update_subject():
    mean = 
    sq_mean = 