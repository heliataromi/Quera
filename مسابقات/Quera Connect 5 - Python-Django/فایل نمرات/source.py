class Grade:
    def __init__(self, stu_id, crc_code, score):
        self.student_id = stu_id
        self.course_code = crc_code
        self.score = score


class CourseUtil:
    def set_file(self, address):
        self.file_address = address

    def load(self, line_number):
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            if line_number <= len(lines):
                raw_grade = lines[line_number - 1].split()
                grade = Grade(int(raw_grade[0]), int(raw_grade[1]), float(raw_grade[2]))
                return grade
            return None

    def calc_student_average(self, student_id):
        grades = []
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            for line in lines:
                raw_grade = [int(line.split()[0]), int(line.split()[1]), float(line.split()[2])]
                if raw_grade[0] == student_id:
                    grades.append(raw_grade)
        average = sum(grade for grade in list(map(lambda x: x[2], grades))) / len(grades)
        return average

    def calc_course_average(self, course_code):
        grades = []
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            for line in lines:
                raw_grade = [int(line.split()[0]), int(line.split()[1]), float(line.split()[2])]
                if raw_grade[1] == course_code:
                    grades.append(raw_grade)
        average = sum(score for score in list(map(lambda x: x[2], grades))) / len(grades)
        return average

    def count(self):
        with open(self.file_address, 'r') as file:
            lines = file.readlines()
            return len(lines)

    def save(self, grade):
        grade_list = [grade.student_id, grade.course_code, grade.score]

        with open(self.file_address, 'r') as file:
            lines = file.readlines()

        with open(self.file_address, 'a') as file:
            for line in lines:
                raw_grade = [int(line.split()[0]), int(line.split()[1]), float(line.split()[2])]
                if raw_grade[0] == grade_list[0] and raw_grade[1] == grade_list[1]:
                    return

            file.write('\n' + ' '.join(map(str, grade_list)))
