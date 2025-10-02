import re


def words_check(input_string):
	input_list = input_string.split()
	result = dict()
	for word in input_list:
		word_characters = list(word)
		for bad_character in re.findall(r'[^A-Za-z]', word):
			word_characters.remove(bad_character)
		if len(word_characters) > len(word) // 2:
			good_word = ''.join(word_characters)
			if good_word.capitalize() in result.keys():
				result[good_word.capitalize()] += 1
			else:
				result[good_word.capitalize()] = 1
	return result
