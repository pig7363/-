class Student:
    def __init__(self, name, student_id):
        self.name = str(name).strip().lower()
        self.student_id = str(student_id).strip()
        self.subjects = {}
        self.grades = {}

# subjects = {과목명: 시험점수}
    def add_subject(self, subject_name, grading):
        from grading import Grading
        self.subject_name = str(subject_name).strip().lower()
        self.grading = Grading(grading)
        self.subjects[subject_name] = grading

    def get_subject_names(self):
        for x in list(self.subjects.keys()):
            return x.capitalize()
    
    def get_subject_score(self, subject_name):
        if subject_name in list(self.subjects.keys()):
            return self.grading
        # ??
        else:
            return -1
        # list(self.subjects.items()) = [영어: 100], [수학: 70], .....
    def compute_gpa(self):
        self.g_point = []
        from grading import Grading
        for v in list(self.subjects.values()):
            if Grading(v).get_grade() == 'A+':
                self.g_point.append(4.5)
            elif Grading(v).get_grade() == 'A':
                self.g_point.append(4)
            elif Grading(v).get_grade() == 'B+':
                self.g_point.append(3.5)
            elif Grading(v).get_grade() == 'B':
                self.g_point.append(3)
            elif Grading(v).get_grade() == 'C+':
                self.g_point.append(2.5)
            elif Grading(v).get_grade() == 'C':
                self.g_point.append(2)
            elif Grading(v).get_grade() == 'D+':
                self.g_point.append(1.5)
            elif Grading(v).get_grade() == 'D':
                self.g_point.append(1)
            else:
                self.g_point.append(0)
        return sum(self.g_point) / len(self.subjects)
    
    def set_subject_grade(self, subject_name, mean, std_dev):
        self.subject_name = subject_name
        self.mean = mean
        self.std_dev = std_dev





    def print_student(self):
        print('-' * 30)
        print('Student ID:', self.student_id)
        print(f'Name: {self.name}')
        print(f'GPA: {self.compute_gpa():.2f}')

        # Condition 14
        for subject in self.subjects.keys():
            grade = self.grades[subject]
            score = self.subjects[subject].raw_score
            print(f' - {subject}: {grade:2s} ({score:5.2f})')

        print('-' * 30)