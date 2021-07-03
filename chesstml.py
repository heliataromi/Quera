import re


def process(name):
	number_of_links = 0
	with open(name, 'r') as file:
		lines = file.readlines()
		for line in lines:
			if re.match(r'(?i)\s*<a([^>]+)>(.+?)</a>', line):
				number_of_links += 1

	return number_of_links
