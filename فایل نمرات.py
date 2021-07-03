class Grade:

	def __init__(self, student_id, course_code, score):
		self.student_id = student_id
		self.course_code = course_code
		self.score = score


class CourseUtil:

	def __init__(self):
		self.file = None
		self.file_lines = None

	def set_file(self, address):
		self.file = open(address, 'r+')
		self.file_lines = self.file.readlines()

	def load(self, line_number):
		if line_number > len(self.file_lines):
			return None
		data = self.file_lines[line_number - 1].split()
		return Grade(data[0], data[1], data[2])

	def save(self, grade):
		data = ' '.join([str(grade.student_id), str(grade.course_code), str(grade.score)])
		self.file.write('\n')
		self.file.write(data)

	def calc_course_average(self, course_code):
		scores = []
		for line in self.file_lines:
			data = line.split()
			if data[1] == course_code:
				scores.append(data[2])

		return sum(scores) / len(scores)

	def calc_student_average(self, student_id):
		scores = []
		for line in self.file_lines:
			data = line.split()
			if data[0] == student_id:
				scores.append(data[2])

		return sum(scores) / len(scores)

	def count(self):
		print(self.file_lines)
		return len(self.file_lines)
