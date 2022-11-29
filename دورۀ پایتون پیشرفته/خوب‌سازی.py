import re


def words_check(text):
    text_list = text.split()
    good_words = {}
    for word in text_list:
        good_word = ''.join(re.findall('[a-zA-Z]', word))
        print(good_word)
        if len(good_word) > len(word) / 2:
            if good_word.title() not in good_words.keys():
                good_words[good_word.title()] = 1
            else:
                good_words[good_word.title()] += 1

    return good_words
