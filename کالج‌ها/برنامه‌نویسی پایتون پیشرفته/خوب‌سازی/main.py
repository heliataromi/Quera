def check_words(text: str) -> dict[str, int]:
    text_list = text.split()

    good_words = {}

    for word in text_list:
        good_word = ''.join(filter(lambda letter: letter.isalpha(), word))

        if len(good_word) > len(word) / 2:
            good_word_title = good_word.title()

            good_words[good_word_title] = good_words.get(good_word.title(), 0) + 1

    return good_words
