import string


def compare(string1, string2):
	pattern = string.ascii_lowercase
	while string1 != '' and string2 != '':
		if pattern.index(string1[0]) < pattern.index(string2[0]):
			string1 = string1[1:]
		elif pattern.index(string2[0]) < pattern.index(string1[0]):
			string2 = string2[1:]
		else:
			string1 = string1[1:]
			string2 = string2[1:]
		if string1 != '' and string2 != '':
			string1 = string1[::-1]
			string2 = string2[::-1]
	if string1 == '' and string2 != '':
		return string2
	elif string1 != '' and string2 == '':
		return string1
	else:
		return 'Both strings are empty!'
